from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import UserModel


class CreateUserViewTests(APITestCase):
    """Тест POST-view создания пользователя."""
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create(username='test_user')
        cls.valid_data = {'username': 'test_user_unique'}
        cls.invalid_data = {'username': 'test_user'}
        cls.url = reverse('createuser')

    def test_successful_request(self):
        """Проверям запрос с валидной датой и получаем 201."""
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 201)

    def test_unsuccessful_request(self):
        """Проверям запрос с невалидной датой и получаем 400."""
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 400)
