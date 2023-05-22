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
        indexes = [
            models.Index(fields=['uuid_token'], name='uuid_token_idx')
        ]

    def __str__(self):
        return self.username


class AudioModel(models.Model):
    """Модель аудио."""
    audio = models.FileField(verbose_name='Аудиозапись')
    uuid = models.UUIDField(
        editable=False, unique=True,
        default=uuid4, verbose_name='UUID-идентификатор аудио')

    def __str__(self):
        return self.audio.name
