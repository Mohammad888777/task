from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from .models import User




def autoCreateTokenForUser(sender,instance,created,**kwargs):

    if created:
        new_token=Token.objects.create(
            user=instance
        )



post_save.connect(autoCreateTokenForUser,sender=User)
