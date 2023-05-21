from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор данных модели пользователя."""
    username = serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )
    uuid_token = serializers.CharField(read_only=True)

    class Meta:
        model = UserModel
        fields = '__all__'

    # def validate(self, attrs):
    #     """Валидация поля 'username'. Имя должно быть уникальным."""
    #     username = attrs.get('username')
    #     if UserModel.objects.filter(username=username).exists():
    #         raise ValidationError(
    #             f'Пользователь с именем {username} уже сущетсвует.'
    #             'Выеберите другое имя.')
    #     return attrs
