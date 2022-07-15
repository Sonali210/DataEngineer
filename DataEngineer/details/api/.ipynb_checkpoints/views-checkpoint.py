from rest_framework.generics import ListAPIView
from details.models import *
from .serializers import *
from django.contrib.postgres import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
   
def home_view(request):
    return render(request, "index.html")
def view5308(request):
    return render(request, "index1.html")
def view5329(request):
    return render(request, "index2.html")


def temp08d(request):
    response = requests.get('http://swar.helper4u.in:2258/tempa')
    temp08d = response.json()
    print(temp08d)
    return JsonResponse("temp08d")
    pass
def temp29d(request):
    response = requests.get('http://swar.helper4u.in:2258/tempb')
    temp29d = response.json()
    print(temp29d)
    return JsonResponse("temp29d")
    pass
def random(request):
    response1 = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=6&max=16&count=11')
    random = response1.json()
#     print(cvc08d)
#     return JsonResponse(cvc08d)
    return render(request, 'index1.html', {'response1':random})
    pass
def cvc08d(request):
    response = requests.get('http://swar.helper4u.in:2258/detailsa')
    cvc08d = response.json()
    print(cvc08d)
#     return JsonResponse(cvc08d)
    return render(request, 'index1.html', {'response':cvc08d})
    pass
def cvc29d(request):
    response = requests.get('http://swar.helper4u.in:2258/detailsb')
    cvc29d = response.json()
    print(cvc29d)
    return JsonResponse(cvc29d)
    pass
class Detail6731ListAPIView(ListAPIView):
    serializer_class = Detail6731Serializer
    queryset = Detail6731.objects.all()
    fields = ('record_index', 'cur_ma_field', 'voltage_v_field', 'capacity_mah_field', 'absolute_time')
    
class Detail6735ListAPIView(ListAPIView):
    serializer_class = Detail6735Serializer
    queryset = Detail6735.objects.all()  
    fields = ('record_index', 'cur_ma_field', 'voltage_v_field', 'capacity_mah_field', 'absolute_time')  
    
class Detailtemp6731ListAPIView(ListAPIView):
    serializer_class = Detailtemp6731Serializer
    queryset = Detailtemp6731.objects.all() 
    fields = ('record_id', 'auxiliary_channel_tu1_t_c_field')
    
class Detailtemp6735ListAPIView(ListAPIView):
    serializer_class = Detailtemp6735Serializer
    queryset = Detailtemp6735.objects.all() 
    fields = ('record_id', 'auxiliary_channel_tu1_t_c_field')
    
