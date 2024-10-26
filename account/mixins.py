from rest_framework.serializers import ValidationError

from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import User,BlockUser

from datetime import datetime,timezone,timedelta



class UserNotLoggedin():

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            raise ValidationError("user already logged in")
        return super().dispatch(request,*args,**kwargs)



class UserNotBLocked():

    def dispatch(self,request,*args,**kwargs):

        now=datetime.now(timezone.utc)
        user_ip=request.META.get("REMOTE_ADDR")

        if BlockUser.objects.filter(
            Q(user_ip=user_ip)&
            Q(blocked_time__gte=now)
        ).exists():
            raise ValidationError("user already blocked try later")
        
        return super().dispatch(request, *args, **kwargs)
        

