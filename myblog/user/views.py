from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from .forms import ProfileForm,ChangepwForm,BlogForm,CommentForm
from account.models import UserProfile,Blog,Comment
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
# class Uhome(View):
    
#     def get(self,request,*args,**kwargs):
#         return render(request,"userhome.html")
# class Uhome(TemplateView):
#     template_name="userhome.html"
class Uhome(CreateView):
    form_class=BlogForm
    template_name="userhome.html"
    
    model=Blog
    success_url=reverse_lazy("uh")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object = form.save()
        messages.success(self.request,"Blog added!")
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']=Blog.objects.all().order_by("-date")
        context['cform']=CommentForm()
        context['comments']=Comment.objects.all()
        return context

def addcomments(request,*args,**kwargs):
    if request.method=="POST":
        bid=kwargs.get("bid")
        blog=Blog.objects.get(id=bid)
        user=request.user
        cmnt=request.POST.get("comment")
        Comment.objects.create(comment=cmnt,user=user,blog=blog)
        messages.success(request,"Comment added succcessfully")
        return redirect("uh")
    else:
        messages.success(request,"Comment failed succcessfully")
        return redirect("uh")

def addlike(request,*args,**kwargs):
    bid=kwargs.get("id")
    blog=Blog.objects.get(id=bid)
    blog.likes.add(request.user)
    blog.save()
    return redirect("uh")




class Profile(TemplateView):
    template_name="profile.html"

class AddProfile(CreateView):
    template_name="addprofile.html"
    form_class=ProfileForm
    model=UserProfile
    success_url=reverse_lazy("pro")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object = form.save()
        messages.success(self.request,"Profile added!")
        return super().form_valid(form)
    # def post(self,request,*args,**kwargs):
    #     form_data=self.form_class(data=request.POST,files=request.FILES)
    #     if form_data.is_valid():
    #         form_data.instance.user=request.user
    #         form_data.save()
    #         messages.success(request,"Profile aded")
    #         return redirect("pro")
    #     else:
    #         return render(request,"addprofile.html",{"form":form_data})
           
class ChangePassword(FormView):
    template_name="changepw.html"
    form_class=ChangepwForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            op=form.cleaned_data.get("old_p")
            np=form.cleaned_data.get("new_p")
            cp=form.cleaned_data.get("cnf_p")
            user=authenticate(request,username=request.user.username,password=op)
            if user:
                if np==cp:
                    user.set_password(np)
                    user.save()
                    logout(request)
                    messages.success(request,"password changed")
                    return redirect("log")
                else:
                    messages.error(request,"password mismatches")
                    return redirect("cpw")
            else:
                messages.error(request,"Old Password is incorrect")
                return redirect("cpw") 
        else:
            messages.error("Changing password failed")
            return redirect("cpw")


# class EditprofileView(View):

    
#     form_class=ProfileForm
#     template_name="editprofile.html"
#     model=UserProfile
    
#     success_url=reverse_lazy("pro")
#     pk_url_kwargs="id"
#     def get(self,request,*args,**kwargs):
#         pid=kwargs.get(self.pk_url_kwargs)
#         p=self.model.objects.get(id=pid)
#         f=self.form_class(instance=p)
#         return render(request,self.template_name,{"form":f})  
#     def post(self,request,*args,**kwargs):
#         pid=kwargs.get(self.pk_url_kwargs)
#         p=self.model.objects.get(id=pid)
#         form_data=self.form_class(data=request.POST,files=request.FILES,instance=p)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Profile updated")
#             return redirect(self.success_url)
#         else:
#             return render(request,self.template_name,{"form":form_data})

        
class EditprofileView(UpdateView):
    form_class=ProfileForm
    template_name="editprofile.html"
    model=UserProfile
    
    success_url=reverse_lazy("pro")
    pk_url_kwargs="pk"
    def form_valid(self,form):
        messages.success(self.request,"Profile updated!")
        self.object = form.save()
        
        return super().form_valid(form)

# class BlogaddForm(CreateView):
#     template_name="userprofile.html"
#     form_class=BlogForm
#     model=Blog
#     success_url=reverse_lazy("uh")
#     def form_valid(self,form):
#         # form.instance.user=self.request.user
#         self.object = form.save()
#         messages.success(self.request,"Blog added!")
#         return super().form_valid(form)


class Myblogs(TemplateView):
    template_name="myblog.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']=Blog.objects.filter(user=self.request.user)
        return context


# class DeleteBlog(View):
    
#     def get(self,request,*args,**kwargs):
#         bid=kwargs.get("id")
#         b=Blog.objects.get(id=bid)
#         b.delete()
#         messages.success(request,"Blog deleted")
#         return redirect("db")
    
class DeleteBlog(DeleteView):
    model=Blog
    success_url=reverse_lazy("mb")
    template_name="deleteblog.html"       

class UserFollowView(View):
    def get(self, request, username):
        # Get the user to follow
        user_to_follow = get_object_or_404(User, username=username)


        userProfile = UserProfile.objects.get(user=request.user)
        userProfile.following.add(user_to_follow)

        return redirect('uh')  # Replace with your redirect or success URL
           
