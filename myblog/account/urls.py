from django.urls import path
from .views import *

urlpatterns=[
    path('reg/',SignUp.as_view(),name="reg"),
    path('log/',SigninView.as_view(),name="log"),
    path('logout/',LogOut.as_view(),name="lgout"),

]

