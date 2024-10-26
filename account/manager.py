from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager
from .validators import validate_phone,validate_email_address
from rest_framework.serializers import ValidationError



class UserManger(BaseUserManager):


    def create_user(self,phone):

        try:
            validate_phone(phone)
        except Exception as e:
            raise ValidationError("phone is not valid")
        
        new_user=self.model(phone=phone)
        new_user.save(using=self._db)

        new_user.set_password(str(new_user.id))

        new_user.is_active=True
        new_user.save(using=self._db)

        return new_user
    


    def create_superuser(self,phone,password,email,username):

        try:
            validate_phone(phone)
        except Exception as e:
            raise ValidationError("phone is not valid")
        
        try:
            validate_email_address(self.normalize_email(email))
        except Exception as e:
            raise ValidationError("email is not valid")
        
        new_superuser=self.model(
            phone=phone,
            email=self.normalize_email(email),
            username=username
        )
        new_superuser.save(using=self._db)
        new_superuser.set_password(password)

        new_superuser.save(using=self._db)

        new_superuser.is_admin=True
        new_superuser.is_active=True
        new_superuser.is_staff=True
        new_superuser.is_superuser=True
        new_superuser.save(using=self._db)


        return new_superuser
    
    

    def get_queryset(self):
        return super().get_queryset().select_related("code")
    





class CodeManger(Manager):

    def get_queryset(self):
        return super().get_queryset().select_related("user")
    






class BlockUserManager(Manager):

    def get_queryset(self):
        return super().get_queryset().select_related("user")
    




        
