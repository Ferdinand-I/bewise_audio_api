from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator, ValidationError

from .models import UserModel, AudioModel


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор данных модели пользователя."""
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )
    uuid_token = serializers.UUIDField(format='hex', read_only=True)

    class Meta:
        model = UserModel
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    """Сериализатор данных модели аудио."""
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=UserModel.objects.all()
    )
    user_uuid_token = serializers.UUIDField(write_only=True)
    audio = serializers.FileField(write_only=True)

    class Meta:
        model = AudioModel
        fields = ['user_id', 'user_uuid_token', 'audio']

    def validate(self, attrs):
        """Аутентификация на уровне сериализатора."""
        if attrs.get('user_id').uuid_token != attrs.get('user_uuid_token'):
            raise AuthenticationFailed(
                'Неверный токен доступа.'
            )
        return attrs

    def validate_audio(self, value: InMemoryUploadedFile):
        """Валидация загружаемого файла."""
        if value.content_type != ('audio/wave' or 'audio/wav'):
            raise ValidationError(
                'Загружаемый файл должен быть в формате "*.wav/*.wave"')
        return value


class URLSerializer(serializers.Serializer):
    """Сериализация URL."""
    url = serializers.URLField()
