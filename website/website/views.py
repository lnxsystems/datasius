
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

import os
from . settings import BASE_DIR


class IndexView(View):

    def get(self, request, **kwargs):

        return render(request, "index.html")


class ProfileView(View):
    
    def get(self, request, **kwargs):

        return render(request, "profile.html")
    
    
    
class BaseView(TemplateView):
    
    template_name = "base.html"