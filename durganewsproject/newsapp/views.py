from django.shortcuts import render

def index(request):
    return render(request, 'newsapp/index.html')

def moviesinfo(request):
   head_msg = 'Latest Movies Information'
   msg1 = 'Pusha Movie is going to break all the records in India'
   msg2 = 'KGF 3 movie is going to release in the 2026 Jan'
   msg3 = 'Salaman Khan has affair with the Miss Universe of India'
   my_dict = {'head_msg': head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
   return render(request, 'newsapp/news.html', context=my_dict)

def politicsinfo(request):
   head_msg = 'Latest Politics Informations'
   msg1 = 'Stocks markets will crash whenever the war will happens'
   msg2 = 'PM Modi is going to America to meet Donal Trump next month'
   msg3 = 'AAM ADMI PARTY leader got caught in corruption'
   my_dict = {'head_msg': head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
   return render(request, 'newsapp/news.html', context=my_dict)

def sportsinfo(request):
   head_msg = 'Latest Sports Information'
   msg1 = 'India lost the Test series againt Austrila'
   msg2 = 'Rishav Pant is on fire this season may he score higest score'
   msg3 = 'Thala Will be seen in this IPL season also'
   my_dict = {'head_msg': head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
   return render(request, 'newsapp/news.html', context=my_dict)

    

def techinfo(request):
   head_msg = 'Latest Technology Information'
   msg1 = 'Tesla is going to come In india very soon'
   msg2 = 'NVDIA has successfully launced his latest AI for us'
   msg3 = 'Many jobs opening will going to come in next month'
   my_dict = {'head_msg': head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
   return render(request, 'newsapp/news.html', context=my_dict)

