from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import (
    authentication_classes,
    permission_classes
    ,throttle_classes,
    api_view
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.serializers import ValidationError
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView

from rest_framework_simplejwt.tokens import RefreshToken

from django.shortcuts import get_object_or_404
from django.db import transaction


from ..validators import validate_phone
from ..models import User,Code

from ..throttle import CustomThrottle

from ..mixins import UserNotLoggedin,UserNotBLocked

from ..utils import createOtpToken

from ..tasks import delete_opt_codes,sendToken


from datetime import datetime,timezone,timedelta






class UserSignIn(
    UserNotLoggedin,
    UserNotBLocked,
    APIView
):
    
    def post(self,request,*args,**kwargs):

        with transaction.atomic():

            data:dict=request.data

            if len(data)>1:
                raise ValidationError("only phone is required")
            
            
            phone=data.get("phone")

            try:
                validate_phone(phone)
            except Exception as e:
                raise ValidationError("phone is not valid or empty")
            
            user=None

            try:
                user=User.objects.get(phone=phone)
            except User.DoesNotExist:
                user=None

            if user:
                user=user
            else:

                user=User.objects.create_user(
                    phone=phone
                )

            new_otp=createOtpToken()
            now=datetime.now(timezone.utc)+timedelta(minutes=3)
            Code.objects.filter(user=user).delete()



            new_code=Code.objects.create(
                exp=now,
                token=new_otp,
                user=user
            )

            s=sendToken.signature(countdown=0.5)
            s.apply_async(args=[str(user.phone),str(new_code.token)])

            
        
                
            return Response({
                    "opt_send":True,
                    "token":user.auth_token.key
                })





class VerifyUser(
    UserNotBLocked,
    APIView
):
    

    permission_classes=[IsAuthenticated]
    authentication_classes=[
        TokenAuthentication
    ]



    def post(self,request,*args,**kwargs):
        
        with transaction.atomic():

            user=request.user
            data:dict=request.data
            now=datetime.now(timezone.utc)

            if len(data)>1:
                raise ValidationError("only otp is required")
            
            if not data.get("otp") or not data.get("otp").isdigit():

                raise ValidationError("otp is required")
            
            try:
                Code.objects.get(
                    token=data.get("otp"),
                    exp__gte=now,
                    user=user
                )

            except Code.DoesNotExist:

                raise ValidationError("otp is not valid or expired")
            
            jwt_token=RefreshToken.for_user(user)

            return Response({
                "access":str(jwt_token.access_token),
                "refresh":str(jwt_token)
            })
            

            





            


            








    
