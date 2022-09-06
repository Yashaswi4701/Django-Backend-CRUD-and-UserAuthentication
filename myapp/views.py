from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import MembersForm
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import SignupForm
# Create your views here.


class HomeView(ListView):
    model=Members
    template_name='home.html'
    
class AddView(CreateView):
    model=Members
    form_class=MembersForm
    template_name='add.html'
    success_url=reverse_lazy('myapp:home')
    
class ModifyView(UpdateView):
    model=Members
    template_name='update.html'
    fields=['name','image','designation','description']
    success_url=reverse_lazy('myapp:home')
    
    
class RemoveView(DeleteView):
    model=Members
    template_name='remove.html'
    success_url=reverse_lazy('myapp:home')
    
    
class SignUpView(CreateView):
    form_class=SignupForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'