from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
   s = '<h1>Hyderabad Jobs Informations </h1>'
   return HttpResponse(s)

def punejobs(request):
   s = '<h1>Pune Jobs Informations </h1>'
   return HttpResponse(s)

def mumbaijobs(request):
   s = '<h1>Mumbai Jobs Informations </h1>'
   return HttpResponse(s)

def banglorejobs(request):
   s = '<h1>Banglore Jobs Informations </h1>'
   return HttpResponse(s)

def chennaijobs(request):
   s = '<h1>Chennai Jobs Informations </h1>'
   return HttpResponse(s)

def noidajobs(request):
   s = '<h1>Noida Jobs Informations </h1>'
   return HttpResponse(s)

