from django.test import TestCase
from ..serializers import UserSerializer


class UserSerializerTests(TestCase):
    """Тесты сериализатора модели пользователя."""
    def test_validate_username(self):
        """Валидация поля 'username'."""
        pass
