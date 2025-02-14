import pytest
from django.core.exceptions import ValidationError

from users.models import User

pytestmark = [pytest.mark.django_db]


def test_create_user():
    user = User.objects.create_user(
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )
    assert user.email == 'test@example.com'
    assert user.is_active
    assert not user.is_staff
    assert user.check_password('testpass123')


def test_create_superuser():
    admin = User.objects.create_superuser(
        email='admin@example.com',
        password='admin123'
    )
    assert admin.is_staff
    assert admin.is_active


def test_user_str_representation():
    user = User.objects.create_user(
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    assert str(user) == 'Test User'

    user.first_name = None
    user.last_name = None
    assert str(user) == 'test@example.com'


def test_email_is_required():
    with pytest.raises(ValueError):
        User.objects.create_user(email='', password='test123') 