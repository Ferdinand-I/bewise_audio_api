from uuid import uuid4

from django.db import models


class UserModel(models.Model):
    """Модель пользователей."""
    username = models.CharField(
        max_length=64, verbose_name='Имя пользователя', unique=True)
    uuid_token = models.UUIDField(
        editable=False, unique=True, default=uuid4, verbose_name='Токен uuid')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.username


class AudioModel(models.Model):
    """Модель аудио."""
    user_id = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name='Пользователь')
    audio = models.FileField(verbose_name='Аудиозапись')
    uuid = models.UUIDField(
        primary_key=True, editable=False, unique=True,
        default=uuid4, verbose_name='UUID-идентификатор аудио'
    )

    class Meta:
        ordering = ['audio']

    def __str__(self):
        return self.audio.name
