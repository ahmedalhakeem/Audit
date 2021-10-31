from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import *
from django.db import IntegrityError
from django.contrib.auth.models import Group
# Create your views here.
def index(request):
    return render(request, 'auditing/index.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']

        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'auditing/login.html') 

def register_reception(request):
    if request.method == 'POST':
        form = Register_Recipient(request.POST or None)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email     = form.cleaned_data['email']
            username  = form.cleaned_data['user_name']
            password   = form.cleaned_data['password']
            confirm   = form.cleaned_data['confirm_password']
            
            if password != confirm:
                return render(request, 'auditing/register_reception.html',{
                    'error': 'الرمز السري غير مطابق, حاول التسجيل مرة اخرى'
                })
            try:
                recipient = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                recipient.groups.add(1)
                recipient.save()
                return HttpResponseRedirect(reverse('index'))
            except IntegrityError:
                return render(request, 'auditing/register_reception.html', {'exist': "اسم المستخدم محجوز مسبقا"})
    
    return render(request, 'auditing/register_reception.html',{'form': Register_Recipient() })            

def reception_formpage(request):
    return render(request, 'auditing/receptionist_frontpage.html')
