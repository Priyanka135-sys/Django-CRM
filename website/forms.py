from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms


class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    class meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='forms-control'
        self.fields['username'].widget.attrs['placeholder']='First Name'
        self.fields['username'].label=" "
        self.fields['username'].help_text="Please enter only alphabets not the charactes"

        self.fields['password1'].widgets.attrs['class']='forms-control'
        self.fields['password1'].widgets.attrs['placeholder']='password'
        self.fields['password1'].label =" "
        self.fields['password1'].help_text="Please enter valid password"
        

        self.fields['password1'].widgets.attrs['class']='forms-control'
        self.fields['password1'].widgets.attrs['placeholder']='password'
        self.fields['password1'].label =" "
        self.fields['password1'].help_text="Please make sure the password matches here!"

        
