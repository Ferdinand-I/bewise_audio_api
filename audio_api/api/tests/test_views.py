from django.shortcuts import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import UserModel


class CreateUserViewTests(APITestCase):
    """Тест POST-view создания пользователя."""
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create(username='test_user')
        cls.valid_data = {'username': 'test_user_unique'}
        cls.invalid_data = {'username': 'test_user'}
        cls.url_user = reverse('createuser')
        cls.url_record = reverse('audio')

    def test_successful_request(self):
        """Проверяем запрос с валидной датой и получаем 201."""
        response = self.client.post(self.url_user, data=self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_not_unique_user(self):
        """Тест создания пользователя с не уникальным 'username'."""
        response = self.client.post(self.url_user, data=self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_request_record_without_query_params(self):
        """Тест view возвращает 404, если был сделан get-запрос
        на эндпоинт '/record/'.
        """
        response = self.client.get(self.url_record)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
