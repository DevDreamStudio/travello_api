from django.db import models
from django.utils.translation import gettext as _

from django.contrib.auth.models import AbstractUser


class CustomSimpleUser(AbstractUser):
    phone_number = models.CharField(max_length=15, verbose_name=_('Номер телефона'), unique=True)
    is_code_checked = models.BooleanField(default=False)
    code = models.CharField(max_length=6, null=True, blank=True)


