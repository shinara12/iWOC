from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Scheduler,History,User
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superadmin', 'is_admin', 'is_user'] 



class SchedulerForm(forms.ModelForm):
    class Meta:
        model=Scheduler
        fields= ['FILE_NAME','UNIQUE_NAME','PROGRAM_NAME','CLIENT_NAME','JOB_TITLE','FREQUENCY','STATUS','OUT_FILE_DIRECTORY']
        widgets={
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'FILE_NAME':forms.TextInput(attrs={'class':'form-control'}),
            'UNIQUE_NAME':forms.TextInput(attrs={'class':'form-control'}),
            'PROGRAM_NAME':forms.TextInput(attrs={'class':'form-control'}),
            'CLIENT_NAME':forms.TextInput(attrs={'class':'form-control'}),
            'JOB_TITLE':forms.TextInput(attrs={'class':'form-control'}),
            'FREQUENCY':forms.Select(attrs={'class':'form-control'}),
            'STATUS':forms.Select(attrs={'class':'form-control'}),
            'OUT_FILE_DIRECTORY':forms.TextInput(attrs={'class':'form-control'})
        }

class HistoryForm(forms.ModelForm):
    class Meta:
        model=History
        fields=['JobIDX','Date','Start','Finish','User','Product','File','Status','Log','ActiveCount','Page','Impression']
      
        widgets={
            'JobIDX':forms.TextInput(attrs={'class':'form-control'}),
            'Date':forms.TextInput(attrs={'class':'form-control'}),
            'Start':forms.TextInput(attrs={'class':'form-control'}),
            'Finish':forms.TextInput(attrs={'class':'form-control'}),
            'User':forms.TextInput(attrs={'class':'form-control'}),
            'Product':forms.Select(attrs={'class':'form-control'}),
            'File':forms.Select(attrs={'class':'form-control'}),
            'Status':forms.TextInput(attrs={'class':'form-control'}),
            'Log':forms.Select(attrs={'class':'form-control'}),
            'ActivityCount':forms.Select(attrs={'class':'form-control'}),
            'Page':forms.TextInput(attrs={'class':'form-control'}),
            'Impression':forms.TextInput(attrs={'class':'form-control'})

        }

