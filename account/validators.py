from rest_framework.serializers import ValidationError
from django.core.validators import validate_email



def validate_phone(value:str):



    if type(value)!=str:
        raise ValidationError("phone type should be string")
    
    if len(value)!=11:
        raise ValidationError("phone length should be 11")
    
    if not value.isdigit():
        raise ValidationError("phone should be only digits")
    
    if not value.startswith("0"):
        raise ValidationError("phone should starts with 0")
    
    
    return value
    



def validate_email_address(value):

    try:
        validate_email(value)
    except Exception as e:
        raise ValidationError("email is not valid")
    
    return value



def validate_chars(value:str):

    if value.isdigit():
        raise ValidationError("only string value is allowed")
    
    if len(value)<3:
        raise ValidationError("min lenght error")
    
    return value