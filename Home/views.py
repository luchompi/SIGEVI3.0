from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class index(LoginRequiredMixin,TemplateView):
    login_url='/auth/login'
    template_name = "Home/index.html"
