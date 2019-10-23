from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    a = {"test":"this is a test message"}
    return render(request,'first_app/index.html',context = a)
