import pytest
from rest_framework import status

from tests.utils import get_url


@pytest.mark.django_db()
class TestDetailTaskView:
    base_url = 'tasks:task_detail'

    def test_return_correct_data_keys(self, client, task):
        response = client.get(get_url(self.base_url, task.id))

        assert list(response.data.keys()) == ['id', 'title', 'description', 'completed', 'created_at']

    def test_correct_status_code(self, client, task):
        response = client.get(get_url(self.base_url, task.id))

        assert response.status_code == status.HTTP_200_OK

    def test_correct_data_type(self, client, task):
        response = client.get(get_url(self.base_url, task.id))

        assert list(map(lambda field: type(field), response.data.values())) == [int, str, str, bool, str]
