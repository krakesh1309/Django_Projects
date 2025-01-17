from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hydjobsinfo(request):
   s = '<h1>Hyderabad Jobs Informantions</h1>'
   return HttpResponse(s)


def punejobsinfo(request):
   s = '<h1>Pune Jobs Informantions</h1>'
   return HttpResponse(s)

def mumbaijobsinfo(request):
   s = '<h1>Mumbai Jobs Informantions</h1>'
   return HttpResponse(s)

def chennaijobsinfo(request):
   s = '<h1>Chennai Jobs Informantions</h1>'
   return HttpResponse(s)

def noidajobsinfo(request):
   s = '<h1>Noida Jobs Informantions</h1>'
   return HttpResponse(s)

