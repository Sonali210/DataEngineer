from rest_framework import serializers
from details.models import *

class Detail6731Serializer(serializers.ModelSerializer):
    record_index = serializers.IntegerField()  
    cur_ma_field = serializers.FloatField()  
    voltage_v_field = serializers.FloatField()  
    capacity_mah_field =serializers.FloatField()    
    absolute_time = serializers.DateTimeField() 
    class Meta:
        model = Detail6731
        fields = ('record_index', 'cur_ma_field', 'voltage_v_field', 'capacity_mah_field', 'absolute_time')

class Detail6735Serializer(serializers.ModelSerializer):
    record_index = serializers.IntegerField()  
    cur_ma_field = serializers.FloatField()  
    voltage_v_field = serializers.FloatField() 
    capacity_mah_field = serializers.FloatField() 
    absolute_time = serializers.DateTimeField() 
    class Meta:
        model = Detail6735
        fields = ('record_index', 'cur_ma_field', 'voltage_v_field', 'capacity_mah_field', 'absolute_time')    

class Detailtemp6731Serializer(serializers.ModelSerializer):
    record_id = serializers.IntegerField()  
    auxiliary_channel_tu1_t_c_field = serializers.FloatField()  
    class Meta:
        model = Detailtemp6731
        fields = ('record_id', 'auxiliary_channel_tu1_t_c_field')
        
class Detailtemp6735Serializer(serializers.ModelSerializer):
    record_id = serializers.IntegerField()  
    auxiliary_channel_tu1_t_c_field = serializers.FloatField() 
    
    class Meta:
        model = Detailtemp6735
        fields = ('record_id', 'auxiliary_channel_tu1_t_c_field')