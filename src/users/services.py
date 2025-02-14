from typing import Optional

from django.contrib.auth import get_user_model
from django.db import transaction

from users.models import User

UserModel = get_user_model()


class UserService:
    @staticmethod
    @transaction.atomic
    def create_user(
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ) -> User:
        user = UserModel.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        return user

    @staticmethod
    def update_user(user: User, **kwargs) -> User:
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def deactivate_user(user: User) -> User:
        user.is_active = False
        user.save()
        return user 