from django import forms
from account.models import UserProfile,Blog,Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']
        
class ChangepwForm(forms.Form):
    old_p=forms.CharField(max_length=100,label="Enter old password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_p=forms.CharField(max_length=100,label="Enter new password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    cnf_p=forms.CharField(max_length=100,label="Re enter new password",widget=forms.PasswordInput(attrs={"class":"form-control"}))

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["title","desc","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "desc":forms.Textarea(attrs={"class":"form-control"}),
            
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["comment"]
        widget:{
            "comment":forms.Textarea(attrs={"class":"form-control"})
        }


