import pytest
from rest_framework import status

from tests.utils import get_url


@pytest.mark.django_db()
class TestDeleteTaskView:
    base_url = 'tasks:task_detail'

    def test_return_correct_data_keys(self, client, task):
        response = client.delete(get_url(self.base_url, task.id))

        assert not response.data

    def test_correct_status_code(self, client, task):
        response = client.delete(get_url(self.base_url, task.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = client.get(get_url(self.base_url, task.id))

        assert response.status_code == status.HTTP_404_NOT_FOUND
