from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserProfile(models.Model):
    phone=models.IntegerField()
    dob=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="profile_pictures",null=True)
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    followers = models.ManyToManyField(User, related_name='following')
   

class Blog(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    image=models.ImageField(upload_to="blog_images",null=True)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="b_user")
    likes=models.ManyToManyField(User,related_name="l_user")

    @property

    def alllikes(self):
        return self.likes.all()

    @property

    def liked_users(self):
        likes=self.likes.all()
        users=[user.username for user in likes]
        return users

class Comment(models.Model):
    comment=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="c_user")
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="c_blog")


