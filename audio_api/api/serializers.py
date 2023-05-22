from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    # user_id = serializers.IntegerField(write_only=True, required=True)
    # user_uuid_token = serializers.UUIDField(
    #     format='hex', write_only=True, required=True)
    audio = serializers.FileField(write_only=True)

    class Meta:
        model = AudioModel
        fields = ['audio']

    def validate_audio(self, value: InMemoryUploadedFile):
        """Валидация загружаемого файла."""
        if value.content_type != 'audio/wave':
            raise ValidationError(
                'Загружаемый файл должен быть в формате "audio/wave"')
        return value
