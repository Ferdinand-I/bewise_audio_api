from uuid import uuid4

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from .models import UserModel
from .serializers import UserSerializer


class CreateUserView(APIView):
    """POST-View для создания пользователя."""
    http_method_names = ['post']

    def post(self, request):
        """Реализация POST-запроса."""
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = UserModel.objects.create(**serializer.initial_data)
            response_data = UserSerializer(user).data
            response_data['uuid_token'] = user.uuid_token.hex()
            return Response(response_data, status=HTTP_201_CREATED)
        return Response('Что-то пошло не так...', status=HTTP_400_BAD_REQUEST)
