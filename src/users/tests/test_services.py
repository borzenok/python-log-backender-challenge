import pytest
from django.db import IntegrityError

from users.services import UserService

pytestmark = [pytest.mark.django_db]


def test_create_user():
    user = UserService.create_user(
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )
    
    assert user.email == 'test@example.com'
    assert user.first_name == 'Test'
    assert user.last_name == 'User'
    assert user.check_password('testpass123')


def test_create_user_duplicate_email():
    UserService.create_user(email='test@example.com', password='test123')
    
    with pytest.raises(IntegrityError):
        UserService.create_user(email='test@example.com', password='test123')


def test_deactivate_user():
    user = UserService.create_user(email='test@example.com', password='test123')
    assert user.is_active
    
    UserService.deactivate_user(user)
    user.refresh_from_db()
    
    assert not user.is_active 