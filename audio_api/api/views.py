import os

from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_201_CREATED,
                                   HTTP_403_FORBIDDEN)
from rest_framework.views import APIView

from .models import UserModel, AudioModel
from .serializers import UserSerializer, AudioSerializer, URLSerializer
from .utils import convert_wav_to_mp3_and_save, make_url


class CreateUserView(APIView):
    """POST-View для создания пользователя."""
    http_method_names = ['post']

    def post(self, request: Request):
        """Реализация POST-запроса."""
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = UserModel.objects.create(**serializer.validated_data)
            return Response(UserSerializer(user).data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class AudioView(APIView):
    """View для добавления и скачивания аудио."""
    http_method_names = ['get', 'post']

    def post(self, request: Request):
        """Реализация POST-запроса."""
        data = request.data
        serializer = AudioSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        user_uuid_token = serializer.validated_data.get('user_uuid_token')
        user = serializer.validated_data.get('user_id')
        # логика аутентификации пользователя
        if not (user.uuid_token == user_uuid_token):
            return Response(
                {'Ошибка': 'Неверный токен доступа.'},
                status=HTTP_403_FORBIDDEN
            )

        audio = serializer.validated_data.get('audio')
        # конвертация
        converted = convert_wav_to_mp3_and_save(audio)
        # создание записи в БД
        audio = AudioModel.objects.create(user_id=user, audio=converted)
        uri = request.build_absolute_uri(reverse('audio'))
        # с помощью кастомной утилиты билдим url
        url = make_url(uri, audio.uuid.hex, user.id)
        serializer = URLSerializer(data={'url': url})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        """Реализация GET-запроса. Скачивание аудио."""
        audio_uuid = request.query_params.get('id')
        try:
            audio = get_object_or_404(AudioModel, uuid=audio_uuid).audio
        except ValidationError as e:
            data = {'Ошибка': e}
            return Response(data, status=HTTP_400_BAD_REQUEST)
        name = os.path.basename(audio.path)
        with open(audio.path, 'rb') as file:
            response = HttpResponse(
                file,
                headers={
                    'Content-Type': 'audio/wave',
                    'Content-Disposition': f'attachment; filename={name}'
                }
            )
        return response
