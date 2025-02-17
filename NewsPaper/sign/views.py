from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from NewsPaper.sign.models import BaseRegisterForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

# Create your views here.
