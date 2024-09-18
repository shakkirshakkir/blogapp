from django.urls import path
from .views import *

urlpatterns=[
    path('uhome/',Uhome.as_view(),name="uh"),
    path('profile/',Profile.as_view(),name="pro"),
    path('addprofile/',AddProfile.as_view(),name="addpro"),
    path('changepwd/',ChangePassword.as_view(),name="cpw"),
    path('editp/<int:pk>',EditprofileView.as_view(),name="epv"),
    path('myb/',Myblogs.as_view(),name="mb"),
    path('delb/<int:pk>',DeleteBlog.as_view(),name="db"),
    path('addc/<int:bid>',addcomments,name="addcmnt"),

    path('addl/<int:id>',addlike,name="addlike"),
    path('user/<str:username>/', UserFollowView.as_view(), name='user_profile'),

    path('user/follow/<str:username>/',UserFollowView.as_view(), name='follow-user'),
    


   


]