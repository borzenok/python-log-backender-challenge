import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        email='test@example.com',
        password='testpass123'
    )


def test_create_user(api_client):
    url = reverse('user-list')
    data = {
        'email': 'new@example.com',
        'password': 'newpass123',
        'first_name': 'New',
        'last_name': 'User'
    }
    
    response = api_client.post(url, data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email='new@example.com').exists()


def test_me_endpoint(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse('user-me')
    
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == user.email 