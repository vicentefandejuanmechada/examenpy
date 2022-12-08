from django.shortcuts import render
from app.models import *
# Create your views here.

def gestion_user(request):
    return render(request,"gestion_users.html")

def crear_user(request):
    