from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # data = {
    #     'title' : 'Home Page',
    #     'body' : 'Welcome to Home page',
    #     'clist' : ['PHP','Java','Python'],
    #     'number' : [12,30,35,40,50],
    #     'std_details' : [
    #         {'name':'khorshed','phone':132435435},
    #         {'name':'emon','phone':235464532},
    #     ]
    # }
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def webCam(request):
    return render(request,'web_cam.html')