import phonenumbers
from django.core.exceptions import ValidationError


def validate_international_phone_number(value):
    try:
        phone_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(phone_number):
            raise ValidationError(f"The phone number '{value}' is not valid in international format.")
        # Check if the number is in international format
        if not phonenumbers.is_possible_number(phone_number):
            raise ValidationError(f"The phone number '{value}' is not in a valid international format.")
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError(f"The phone number '{value}' is not a valid phone number.")
