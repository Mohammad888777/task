from celery import shared_task

from django.shortcuts import get_object_or_404


from .models import User
from .utils import convert_str_to_uuid,send_otp




@shared_task(
    name="delete user otps",
    bind=True
)

def delete_opt_codes(self,user_id):

    try:
        id=convert_str_to_uuid(str(user_id))

        user=get_object_or_404(User,id=user_id)

        user.code.delete()

    except Exception as e:

        print("ERORORORR",e)

        self.retry(
            max_retries=5,
            countdown=5
        )





@shared_task(
    name="send otp",bind=True
)
def sendToken(self,user_phone,token):

    try:
        send_otp(user_phone,token)
        
    except Exception as e:
        print("######")
        print("######")
        print(e)
        print("######")
        print("######")
        
        self.retry(
            max_retries=5,
            countdown=2
        )
