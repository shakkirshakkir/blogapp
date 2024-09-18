from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,CreateView,TemplateView,FormView
from .forms import SignupForm,SigninForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# class Mhome(View):
#     def get(self,request,*args,**kwargs):
   
#         return render(request,"mhome.html")
class Mhome(TemplateView):
    template_name="mhome.html"

# class SignUp(View):

#     def get(self,request,*args,**kwargs):
#         f=SignupForm()
#         return render(request,"reg.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#         form_data=SignupForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User registered sucessfully")
            
#             return redirect("h")
                      
#         else:
#             return render(request,"reg.html",{"f":form_data})

class SignUp(CreateView):
    form_class=SignupForm
    template_name="reg.html"
    model=User
    success_url=reverse_lazy("log")



# class SigninView(View):


#     def get(self,request):
#         f=SigninForm()
        
#         return render(request,"log.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#         form_data=SigninForm(data=request.POST)
#         if form_data.is_valid():
#             un=form_data.cleaned_data.get("username")
#             ps=form_data.cleaned_data.get("password")
#             user=authenticate(request,username=un,password=ps)
#             if user:
#                 login(request,user)
#                 messages.success(request,"login completed")
#                 return redirect("uh")
#             else:
#                 messages.error(request,"login failed")
#                 return redirect("log")

#         else:
#             messages.error(request,"login failed")
#             return render(request,"log.html",{"form":form_data}) 

class SigninView(FormView):
    template_name="log.html"
    form_class=SigninForm
    def post(self,request,*args,**kwargs):
        form_data=SigninForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                login(request,user)
                messages.success(request,"login completed")
                return redirect("uh")
            else:
                messages.error(request,"login failed")
                return redirect("log")

        else:
            messages.error(request,"login failed")
            return render(request,"log.html",{"form":form_data}) 

class LogOut(View):
    def get(self,request):

        logout(request)
        return redirect("log")

def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=request.user)

    if user_to_follow != request.user:  # Ensure user isn't trying to follow themselves
        if user_to_follow not in user_profile.followers.all():
            user_profile.followers.add(user_to_follow)
        else:
            user_profile.followers.remove(user_to_follow)

    return redirect('user-profile', username=username)

