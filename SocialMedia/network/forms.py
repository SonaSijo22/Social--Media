from django import forms

from network.models import Profile,Post,Like,Comment

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]
    
class LoginForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

class ProfileForm(forms.ModelForm):

  class Meta:

    model=Profile

    exclude=['created_date','updated_date','is_active']

    widgets={

            # 'name':forms.TextInput(attrs={'class':"form-control"}),

            "profile_image":forms.FileInput(attrs={'class':'forms-control'}),

            'bio':forms.TextInput(attrs={'class':"form-control"}),

            "dob":forms.TextInput(attrs={'class':'forms-control'}),

            'email':forms.TextInput(attrs={'class':'forms-control'})


        }

class PostForm(forms.ModelForm):
    
    class Meta:

        model = Post

        exclude=["created_date","user_object","is_active","updtaed_date","like",]

        widgets={

            'caption':forms.TextInput(attrs={'class':"form-control"}),

            "post_image":forms.FileInput(attrs={'class':'forms-control'})
        }

class CommentForm(forms.ModelForm):

    class Meta:

        model=Comment

        fields=['comment']

        widgets={

            'comment':forms.TextInput(attrs={'class':"form-control"})
        }
        labels={'comment':'write your comment'}
