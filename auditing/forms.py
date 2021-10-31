from .models import *
from django import forms

class Register_Recipient(forms.Form):
    first_name = forms.CharField(label='الاسم الاول', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "ادخل الاسم الاول"}))
    last_name = forms.CharField(label="الاسم الاخير", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل الاسم الاخير'}))
    user_name= forms.CharField(label="اسم المستخدم", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل اسم المستخدم'}))
    email = forms.EmailField(label='البريد الالكتروني', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "ادخل البريد الالكتروني"}))
    password = forms.CharField(label="ادخل الرمز السري",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "ادخل الرمز السري"}))
    confirm_password = forms.CharField(label="اعد كتابة الرمز السري", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "اعد كتابة الرمز السري"}))
