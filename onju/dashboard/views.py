from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("hi there")

# Create your views here.
