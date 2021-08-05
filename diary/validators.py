from django.core.exceptions import ValidationError

def validate_no_hash(value):
    if '#' in value:
        raise ValidationError('You can`t include the #.')

def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError('you can`t include the number.')

def validate_score(value):
    if value < 0 or value > 10:
        raise ValidationError('You can input from 0 to 10.')