import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_email_domain(email: str) -> None:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError(
            _('%(email)s is not a valid email address'),
            params={'email': email},
        ) 