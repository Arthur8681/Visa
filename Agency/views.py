from django.shortcuts import render
from .models import *
# Create your views here.

def show(request):
    return render(request, 'main.html')