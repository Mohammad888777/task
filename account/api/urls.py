from django.urls import path,include
from . import views





urlpatterns=[

    path("login/",views.UserSignIn.as_view(),name="login"),
    path("verify/",views.VerifyUser.as_view(),name="verify"),
    
]