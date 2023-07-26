import json

import pytest
from rest_framework import status

from tests.utils import get_url


@pytest.mark.django_db()
class TestCreateTaskView:
    base_url = 'tasks:task_list'

    initial_data = {
        'title': 'test',
        'description': 'test'
    }

    def test_return_correct_data_keys(self, client):
        response = client.post(get_url(self.base_url), data=json.dumps(self.initial_data),
                               content_type='application/json')

        assert list(response.data.keys()) == ['id', 'title', 'description', 'completed', 'created_at']

    def test_correct_status_code(self, client):
        response = client.post(get_url(self.base_url), content_type='application/json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response = client.post(get_url(self.base_url), data=json.dumps(self.initial_data),
                               content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_correct_data_type(self, client):
        response = client.post(get_url(self.base_url), data=json.dumps(self.initial_data),
                               content_type='application/json')

        assert list(map(lambda field: type(field), response.data.values())) == [int, str, str, bool, str]

    def test_correct_require_fields_validation(self, client):
        response = client.post(get_url(self.base_url), content_type='application/json')

        data = response.data

        assert data.get('title', None) == ['Обязательное поле.']
        assert data.get('description', None) == ['Обязательное поле.']

    def test_correct_unique_title_validation(self, client, task):
        initial_data = {
            'title': task.title,
            'description': 'test'
        }

        response = client.post(get_url(self.base_url), data=json.dumps(initial_data),
                               content_type='application/json')

        assert response.data.get('title', None) == ['Задача с таким Заголовок уже существует.']

    def test_create_data_correctness(self, client):
        response = client.post(get_url(self.base_url), data=json.dumps(self.initial_data),
                               content_type='application/json')

        data = response.data

        assert data.get('title', None) == self.initial_data.get('title')
        assert data.get('description', None) == self.initial_data.get('description')
        assert not data.get('completed', None)
        assert data.get('created_at', None)
