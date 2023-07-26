import json

import pytest
from rest_framework import status

from tests.utils import get_url


@pytest.mark.django_db()
class TestUpdateTaskView:
    base_url = 'tasks:task_detail'

    initial_data = {
        'title': 'test',
        'description': 'test',
        'completed': True
    }

    def test_return_correct_data_keys(self, client, task):
        response = client.patch(get_url(self.base_url, task.id), data=json.dumps(self.initial_data),
                                content_type='application/json')

        assert list(response.data.keys()) == ['id', 'title', 'description', 'completed', 'created_at']

    def test_correct_status_code(self, client, task):
        response = client.patch(get_url(self.base_url, task.id), data=json.dumps(self.initial_data),
                                content_type='application/json')

        assert response.status_code == status.HTTP_200_OK

    def test_correct_data_type(self, client, task):
        response = client.patch(get_url(self.base_url, task.id), data=json.dumps(self.initial_data),
                                content_type='application/json')

        assert list(map(lambda field: type(field), response.data.values())) == [int, str, str, bool, str]

    def test_read_only_fields_immutability(self, client, task):
        initial_data = {
            'id': 20,
            'created_at': None
        }

        response = client.patch(get_url(self.base_url, task.id), data=json.dumps(initial_data),
                                content_type='application/json')

        data = response.data

        assert data.get('id', None) == task.id
        assert data.get('created_at', None) == task.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    def test_update_data_correctness(self, client, task):
        response = client.patch(get_url(self.base_url, task.id), data=json.dumps(self.initial_data),
                                content_type='application/json')

        data = response.data

        assert data.get('title', None) == self.initial_data.get('title')
        assert data.get('description', None) == self.initial_data.get('description')
        assert data.get('completed', None) == self.initial_data.get('completed')
