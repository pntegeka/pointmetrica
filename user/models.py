import uuid

from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext as _
from django.db import models
from django.utils.timezone import now
from datetime import timedelta

from business.models import Location, Business


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('Users require a phone number field')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255, )
    email = models.EmailField(_('email address'), blank=True, null=True)
    phone_number = PhoneNumberField(_('phone number'), unique=True, )
    first_name = models.CharField(_('first name'), max_length=255, )
    middle_name = models.CharField(_('middle name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=255, )
    created_date = models.DateTimeField(auto_now_add=True)
    hand_held_device_token = models.CharField(max_length=255, blank=True, null=True)
    user_profile_image = models.ImageField(upload_to='user_profile_images/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission, verbose_name=_('user permissions'), blank=True, related_name='custom_user_set'
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ['-created_date']

    def get_username(self):
        return f'{self.phone_number}'

    def __str__(self):
        return f'{self.phone_number}'

    @staticmethod
    def tokens():
        return ''

    def get_full_name(self):
        if self.middle_name:
            full_name = (f"{self.first_name.strip().capitalize()} {self.middle_name.strip().capitalize()} "
                         f"{self.last_name.strip().capitalize()}")
        else:
            full_name = f"{self.first_name.strip().capitalize()} {self.last_name.strip().capitalize()}"

        return full_name.strip()


class Owner(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Unknown'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner_profiles', )
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, default=3)
    date_of_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(
        Location,
        blank=True,
        related_name='location_owners'
    )
    business = models.ManyToManyField(
        Business,
        blank=True,
        related_name='business_owners'
    )
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user


class Manager(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Unknown'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='manager_profiles', )
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, default=3)
    date_of_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(
        Location,
        blank=True,
        related_name='location_regional_managers'
    )
    business = models.ManyToManyField(
        Business,
        blank=True,
        related_name='business_regional_managers'
    )
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user


class Supervisor(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Unknown'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='supervisor_profiles', )
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, default=3)
    date_of_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(
        Location,
        blank=True,
        related_name='location_supervisors'
    )
    business = models.ManyToManyField(
        Business,
        blank=True,
        related_name='business_supervisors'
    )
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user


class SalesAgent(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Unknown'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sales_agent_profiles', )
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, default=3)
    date_of_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(
        Location,
        blank=True,
        related_name='location_sales_agents'
    )
    business = models.ManyToManyField(
        Business,
        blank=True,
        related_name='business_sales_agents'
    )
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user


class SupportAnalyst(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Unknown'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='support_analyst_profiles', )
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, default=3)
    date_of_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(
        Location,
        blank=True,
        related_name='location_support_analysts'
    )
    business = models.ManyToManyField(
        Business,
        blank=True,
        related_name='business_support_analysts'
    )
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user


class DeliveryStaff(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Unknown'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='delivery_staff_profiles', )
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, default=3)
    date_of_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(
        Location,
        blank=True,
        related_name='location_delivery_staff'
    )
    business = models.ManyToManyField(
        Business,
        blank=True,
        related_name='business_delivery_staff'
    )
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user