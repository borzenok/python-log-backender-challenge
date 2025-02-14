from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Administrator'
    MANAGER = 'manager', 'Manager'
    USER = 'user', 'User'


EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 