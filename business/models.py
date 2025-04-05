import uuid
from datetime import date, timedelta

import uuid
from django.db import models
from django.db.models import ProtectedError
from django_countries.fields import CountryField

from business.utils import validate_international_phone_number


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    country = CountryField(blank_label="(Select country)", default="UG")
    address = models.CharField(max_length=255)
    primary_phone_contact = models.CharField(
        max_length=20,
        validators=[validate_international_phone_number],
    )
    alternative_phone_contact = models.CharField(
        max_length=20,
        validators=[validate_international_phone_number],
    )
    primary_email_contact = models.EmailField(null=False, blank=False)
    alternative_email_contact = models.EmailField(null=True, blank=True)
    tax_Id_number = models.CharField(max_length=255, blank=True, null=True)
    accounts_currency = models.CharField(
        max_length=255, default='UGX'
    )
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    business_logo = models.ImageField(upload_to='business_logo/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}'