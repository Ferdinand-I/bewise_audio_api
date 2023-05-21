from uuid import uuid4

from django.db import models


class UserModel(models.Model):
    """Модель пользователей."""
    username = models.CharField(
        max_length=64, verbose_name='Имя пользователя', unique=True)
    uuid_token = models.BinaryField(verbose_name='Токен доступа')

    class Meta:
        ordering = ['pk']
        indexes = [
            models.Index(fields=['uuid_token'], name='uuid_token_idx')
        ]

    def save(self, *args, **kwargs):
        """Переопределяем метод .save() чтобы автоматически генерировать
        токен и сохранять его в БД.
        """
        self.uuid_token = uuid4().bytes
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username