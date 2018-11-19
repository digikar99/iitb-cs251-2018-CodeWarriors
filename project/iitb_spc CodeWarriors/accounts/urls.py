from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views
from django.conf.urls import url

from . import views


urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
]


