from rest_framework.generics import ListAPIView
from details.models import *
from .serializers import *
from django.contrib.postgres import fields

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