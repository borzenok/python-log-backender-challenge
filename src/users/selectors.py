from typing import Optional

from django.db.models import QuerySet

from users.models import User


def user_list(*, is_active: Optional[bool] = None) -> QuerySet[User]:
    filters = {}
    
    if is_active is not None:
        filters['is_active'] = is_active
        
    qs = User.objects.filter(**filters)
    return qs


def get_user_by_email(*, email: str) -> Optional[User]:
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None 