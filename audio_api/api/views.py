from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from .models import UserModel, AudioModel
from .serializers import UserSerializer, AudioSerializer


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
        if serializer.is_valid():
            audio = AudioModel.objects.create(**serializer.validated_data)
            return Response(AudioSerializer(audio).data)

    def get(self, request: Request):
        """Реализация GET-запроса."""
        pass
