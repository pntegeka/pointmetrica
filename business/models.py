import uuid
from django.db import models
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
    company_registration_number = models.CharField(max_length=255, null=True, blank=True)
    accounts_currency = models.CharField(
        max_length=255, default='UGX'
    )
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    business_logo = models.ImageField(upload_to='business_logo/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    contacts_verified = models.BooleanField(default=False)
    registration_information_verified = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE,
                                 related_name='business_locations', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    altitude = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    archived = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    business = models.ForeignKey(Business, on_delete=models.CASCADE,
                                 related_name='business_customers', null=True, blank=True)
    primary_phone_contact = models.CharField(
        max_length=20,
        validators=[validate_international_phone_number],
    )
    alternative_phone_contact = models.CharField(
        max_length=20,
        validators=[validate_international_phone_number],
        null=True,
        blank=True
    )
    tax_Id_number = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    company_registration_number = models.CharField(max_length=255, null=True, blank=True)
    is_institution = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    contacts_verified = models.BooleanField(default=False)
    registration_information_verified = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'Batch {self.name}'


class CustomerPersonnel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE,
        related_name='customer_personnel'
    )
    full_name = models.CharField(max_length=255)
    national_Id_number = models.CharField(max_length=255,null=True, blank=True)
    refugee_Id_number = models.CharField(max_length=255, null=True, blank=True)
    passport_Id_number = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255)
    primary_phone_contact = models.CharField(
        max_length=20,
        validators=[validate_international_phone_number],
    )
    alternative_phone_contact = models.CharField(
        max_length=20,
        validators=[validate_international_phone_number],
        null=True,
        blank=True
    )
    primary_email_contact = models.EmailField(null=False, blank=False)
    alternative_email_contact = models.EmailField(null=True, blank=True)
    is_finance_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    contacts_verified = models.BooleanField(default=False)
    registration_information_verified = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'Batch {self.full_name} - {self.customer.name}'


class CustomerLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='customer_locations', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    altitude = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    archived = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}'


class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE,
                                 related_name='business_product_categories', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    archived = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                 related_name='business_category_products', null=True, blank=True)
    name = models.CharField(max_length=255)
    transaction_unit = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}'


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 related_name='location_inventory')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_inventory')
    quantity_available = models.DecimalField(max_digits=15, decimal_places=2)
    quantity_available_value = models.DecimalField(max_digits=15, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'Batch {self.location.name} - {self.product.name}'