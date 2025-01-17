import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'djproject.setting')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake = Faker()
def phonenumber():
   d1 = randint(7,9)
   num = ''+str(d1)
   for i in range(9):
      num = num+str(randint(0,9))

   return int(num)

def populate(n):
   for i in range(n):
      fdate = fake.date()
      fcompany = fake.company()
      ftitle= fake.random_element(elements=('Project Manager', 'teamLead', 'Softwere Engineer'))
      feligibility = fake.random_element(elements=('B.tech', 'M.tech', 'MCA', 'Phd'))
      faddress = fake.address()
      femail = fake.email()
      fphonenumber = phonenumbergen()
      hydjobs_record=hydjobs.get_or_created(date=fdate, company=fcompany,title= ftitle,eligibility =feligibility, address = faddress, email= femail, phonenumber= fphonenumber)
   populate(30)