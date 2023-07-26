import pytest
from rest_framework import status

from tests.factories import TaskFactory
from tests.utils import get_url


@pytest.mark.django_db()
class TestListTaskView:
    base_url = 'tasks:task_list'

    def test_return_correct_data_keys(self, client):
        TaskFactory.create_batch(5)

        response = client.get(get_url(self.base_url))

        assert list(response.data[0].keys()) == ['id', 'title', 'description', 'completed', 'created_at']

    def test_correct_status_code(self, client):
        TaskFactory.create_batch(5)

        response = client.get(get_url(self.base_url))

        assert response.status_code == status.HTTP_200_OK

    def test_correct_data_type(self, client):
        TaskFactory.create_batch(5)

        response = client.get(get_url(self.base_url))

        assert list(map(lambda field: type(field), response.data[0].values())) == [int, str, str, bool, str]

    @pytest.mark.parametrize("completed", [True, False])
    def test_correct_completed_field_filter(self, client, completed):
        amount = 5

        TaskFactory.create_batch(amount, completed=completed)

        response = client.get(get_url(self.base_url, completed=completed))

        assert len(response.data) == amount
        assert all(item.get('completed', None) for item in response.data) == completed
