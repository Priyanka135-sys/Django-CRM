from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


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

        self.fields['password1'].widget.attrs['class']='forms-control'
        self.fields['password1'].widget.attrs['placeholder']='password'
        self.fields['password1'].label =" "
        self.fields['password1'].help_text="Please enter valid password"
        

        self.fields['password1'].widget.attrs['class']='forms-control'
        self.fields['password1'].widget.attrs['placeholder']='password'
        self.fields['password1'].label =" "
        self.fields['password1'].help_text="Please make sure the password matches here!"



#ADD record


class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'First Name','class':'forms-control'}))
    last_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name','class':'forms-control'}))

    email=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Email','class':'forms-control'}))
    phone=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Phone','class':'forms-control'}))
    address=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'full Address','class':'forms-control'}))
    city=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'City Name','class':'forms-control'}))
    state=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'State Name','class':'forms-control'}))
    zipcode=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Zipcode','class':'forms-control'}))



    class Meta:
        model=Record
        exclude=("user",)

