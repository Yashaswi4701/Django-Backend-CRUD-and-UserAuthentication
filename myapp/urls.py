from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new
from .views import AddView
from .views import ModifyView
from . views import RemoveView
from .views import SignUpView

from .views import HomeView
app_name='myapp'

urlpatterns = [
    path("home/", HomeView.as_view() ,name='home'),
    path('home/add/',AddView.as_view(),name='add'),
    path('home/modify/<pk>/',ModifyView.as_view(),name='modify'),
    path('home/remove/<pk>/',RemoveView.as_view(),name='modify'),
    path('home/signup/',SignUpView.as_view(),name='signup'),
    
] 