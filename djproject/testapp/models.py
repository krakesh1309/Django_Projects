from django.db import models

# Create your models here.
class hydjobs(models.Model):
   date = models.DateField();
   comapny = models.CharField(max_length=100);
   title = models.CharField(max_length=100);
   eligibility = models.CharField(max_length=100);
   address = models.CharField(max_length=100);
   email = models.EmailField();
   phonenumber = models.IntegerField()

class blorejobs(models.Model):
   date = models.DateField();
   comapny = models.CharField(max_length=100);
   title = models.CharField(max_length=100);
   eligibility = models.CharField(max_length=100);
   address = models.CharField(max_length=100);
   email = models.EmailField();
   phonenumber = models.IntegerField()

class punejobs(models.Model):
   date = models.DateField();
   comapny = models.CharField(max_length=100);
   title = models.CharField(max_length=100);
   eligibility = models.CharField(max_length=100);
   address = models.CharField(max_length=100);
   email = models.EmailField();
   phonenumber = models.IntegerField()

class chennaijobs(models.Model):
   date = models.DateField();
   comapny = models.CharField(max_length=100);
   title = models.CharField(max_length=100);
   eligibility = models.CharField(max_length=100);
   address = models.CharField(max_length=100);
   email = models.EmailField();
   phonenumber = models.IntegerField()