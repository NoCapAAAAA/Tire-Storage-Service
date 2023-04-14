from django.core.exceptions import ValidationError


def validate_phone_number(phone):
    allowed_chars = '+1234567890'
    for i in phone:
        if i not in allowed_chars:
            raise ValidationError('Номер телефона может содержать лишь цифры')