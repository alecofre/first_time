from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from time import gmtime, strftime
# Create your views here.
def home(request):
     context = {
          'time' : strftime('%Y-%m-%d %H:%M:%S %p', gmtime())
     }
     return render(request,'time_display/home.html', context)
     return HttpResponse('entré a la pagina')