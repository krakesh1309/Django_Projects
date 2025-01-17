from django.contrib import admin
from django.urls import path
from urlsApp import views

urlpatterns = [
   path('hydjobsinfo/', views.hydjobsinfo),
   path('punejobsinfo/', views.punejobsinfo),
   path('mumbaijobsinfo/', views.mumbaijobsinfo),
   path('chennaijobsinfo/', views.chennaijobsinfo),
   path('noidajobsinfo/', views.noidajobsinfo),

]
