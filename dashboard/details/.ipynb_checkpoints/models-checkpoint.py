# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models 

class Cycle6731(models.Model):
    channel = models.BigIntegerField()  
    total_of_cycle = models.BigIntegerField(blank=True, null=True)
    capacity_of_charge_mah_field = models.FloatField(blank=True, null=True)  
    capacity_of_discharge_mah_field = models.FloatField(blank=True, null=True)  
    cycle_life_field = models.FloatField(blank=True, null=True) 


class Cycle6735(models.Model):
    channel = models.BigIntegerField() 
    total_of_cycle = models.BigIntegerField(blank=True, null=True) 
    capacity_of_charge_mah_field = models.FloatField(blank=True, null=True) 
    capacity_of_discharge_mah_field = models.FloatField(blank=True, null=True) 
    cycle_life_field = models.FloatField(blank=True, null=True)  


class Detailtemp6731(models.Model):
    record_id = models.BigIntegerField() 
    step_name = models.TextField(blank=True, null=True)
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    realtime = models.DateTimeField(blank=True, null=True)  
    auxiliary_channel_tu1_t_c_field = models.FloatField(blank=True, null=True)  
    gap_of_temperature = models.BigIntegerField(blank=True, null=True)

class Detailtemp6735(models.Model):
    record_id = models.BigIntegerField()
    step_name = models.TextField(blank=True, null=True)
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    realtime = models.DateTimeField(blank=True, null=True)  
    auxiliary_channel_tu1_t_c_field = models.FloatField(blank=True, null=True) 
    gap_of_temperature = models.BigIntegerField(blank=True, null=True) 


class Detailvol6731(models.Model):
    record_id = models.BigIntegerField()
    step_name = models.TextField(blank=True, null=True)
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    realtime = models.DateTimeField(blank=True, null=True) 
    auxiliary_channel_tu1_u_v_field = models.FloatField(blank=True, null=True) 
    gap_of_voltage = models.BigIntegerField(blank=True, null=True) 


class Detailvol6735(models.Model):
    record_id = models.BigIntegerField()
    step_name = models.TextField(blank=True, null=True)  
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True)
    realtime = models.DateTimeField(blank=True, null=True)
    auxiliary_channel_tu1_u_v_field = models.FloatField(blank=True, null=True) 
    gap_of_voltage = models.BigIntegerField(blank=True, null=True) 


class Detail6731(models.Model):
    record_index = models.BigIntegerField()  
    status = models.TextField(blank=True, null=True)  
    jumpto = models.BigIntegerField(blank=True, null=True)  
    cycle = models.BigIntegerField( blank=True, null=True)  
    step = models.BigIntegerField(blank=True, null=True) 
    cur_ma_field = models.FloatField(blank=True, null=True)  
    voltage_v_field = models.FloatField(blank=True, null=True)  
    capacity_mah_field = models.FloatField(blank=True, null=True)  
    energy_mwh_field = models.FloatField(blank=True, null=True) 
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    absolute_time = models.DateTimeField(blank=True, null=True) 


class Detail6735(models.Model):
    record_index = models.BigIntegerField() 
    status = models.TextField(blank=True, null=True)  
    jumpto = models.BigIntegerField(blank=True, null=True)  
    cycle = models.BigIntegerField(blank=True, null=True)  
    step = models.BigIntegerField(blank=True, null=True)  
    cur_ma_field = models.FloatField(blank=True, null=True)  
    voltage_v_field = models.FloatField(blank=True, null=True) 
    capacity_mah_field = models.FloatField(blank=True, null=True) 
    energy_mwh_field = models.FloatField(blank=True, null=True) 
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    absolute_time = models.DateTimeField(blank=True, null=True) 


class Statis6731(models.Model):
    channel = models.BigIntegerField(blank=True, null=True)  
    cycle = models.BigIntegerField(blank=True, null=True) 
    step = models.BigIntegerField(blank=True, null=True)  
    raw_step_id = models.BigIntegerField(blank=True, null=True)  
    status = models.TextField(blank=True, null=True)  
    start_voltage_v_field = models.FloatField(blank=True, null=True)
    end_voltage_v_field = models.FloatField(blank=True, null=True) 
    start_current_ma_field = models.FloatField(blank=True, null=True)  
    end_current_ma_field = models.FloatField(blank=True, null=True)  
    capacity_mah_field = models.FloatField(blank=True, null=True)  
    endure_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True) 
    absolute_time = models.DateTimeField(blank=True, null=True) 
    discharge_capacity_mah_field = models.FloatField(blank=True, null=True) 
    charge_capacity_mah_field = models.FloatField(blank=True, null=True)  
    discharge_capacity_mah_1 = models.FloatField(blank=True, null=True) 
    net_engy_dchg_mwh_field = models.FloatField(blank=True, null=True)
    engy_chg_mwh_field = models.FloatField(blank=True, null=True) 
    engy_dchg_mwh_field = models.FloatField(blank=True, null=True) 

class Statis6735(models.Model):
    channel = models.BigIntegerField(blank=True, null=True)  
    cycle = models.BigIntegerField(blank=True, null=True)  
    step = models.BigIntegerField(blank=True, null=True)  
    raw_step_id = models.BigIntegerField(blank=True, null=True) 
    status = models.TextField(blank=True, null=True)  
    start_voltage_v_field = models.FloatField(blank=True, null=True) 
    end_voltage_v_field = models.FloatField(blank=True, null=True) 
    start_current_ma_field = models.FloatField(blank=True, null=True) 
    end_current_ma_field = models.FloatField(blank=True, null=True)  
    capacity_mah_field = models.FloatField(blank=True, null=True)  
    endure_time_h_min_s_ms_field = models.TextField(blank=True, null=True)  
    relative_time_h_min_s_ms_field = models.TextField(blank=True, null=True)
    absolute_time = models.DateTimeField(blank=True, null=True) 
    charge_capacity_mah_field = models.FloatField(blank=True, null=True) 
    discharge_capacity_mah_field = models.FloatField(blank=True, null=True) 
    net_engy_dchg_mwh_field = models.FloatField(blank=True, null=True)  
    engy_chg_mwh_field = models.FloatField(blank=True, null=True) 
    engy_dchg_mwh_field = models.FloatField(blank=True, null=True) 