# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cycle6735(models.Model):
    channel = models.BigIntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    total_of_cycle = models.BigIntegerField(db_column='ToTal of Cycle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capacity_of_charge_mah_field = models.FloatField(db_column='Capacity of charge(mAh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    capacity_of_discharge_mah_field = models.FloatField(db_column='Capacity of discharge(mAh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cycle_life_field = models.FloatField(db_column='Cycle Life(%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = 'Cycle_67_3_5'


class Detailtemp6735(models.Model):
    record_id = models.BigIntegerField(db_column='Record ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    step_name = models.TextField(db_column='Step Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relative_time_h_min_s_ms_field = models.TextField(db_column='Relative Time(h:min:s.ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    realtime = models.DateTimeField(db_column='Realtime', blank=True, null=True)  # Field name made lowercase.
    auxiliary_channel_tu1_t_c_field = models.FloatField(db_column='Auxiliary channel TU1 T(°C)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gap_of_temperature = models.BigIntegerField(db_column='Gap of Temperature', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'DetailTemp_67_3_5'


class Detailvol6735(models.Model):
    record_id = models.BigIntegerField(db_column='Record ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    step_name = models.TextField(db_column='Step Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relative_time_h_min_s_ms_field = models.TextField(db_column='Relative Time(h:min:s.ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    realtime = models.DateTimeField(db_column='Realtime', blank=True, null=True)  # Field name made lowercase.
    auxiliary_channel_tu1_u_v_field = models.FloatField(db_column='Auxiliary channel TU1 U(V)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gap_of_voltage = models.BigIntegerField(db_column='Gap of Voltage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'DetailVol_67_3_5'


class Detail6735(models.Model):
    record_index = models.BigIntegerField(db_column='Record Index', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    jumpto = models.BigIntegerField(db_column='JumpTo', blank=True, null=True)  # Field name made lowercase.
    cycle = models.BigIntegerField(db_column='Cycle', blank=True, null=True)  # Field name made lowercase.
    step = models.BigIntegerField(db_column='Step', blank=True, null=True)  # Field name made lowercase.
    cur_ma_field = models.FloatField(db_column='Cur(mA)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    voltage_v_field = models.FloatField(db_column='Voltage(V)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    capacity_mah_field = models.FloatField(db_column='CapaCity(mAh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    energy_mwh_field = models.FloatField(db_column='Energy(mWh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    relative_time_h_min_s_ms_field = models.TextField(db_column='Relative Time(h:min:s.ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    absolute_time = models.DateTimeField(db_column='Absolute Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Detail_67_3_5'


class Statis6735(models.Model):
    channel = models.BigIntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    cycle = models.BigIntegerField(db_column='CyCle', blank=True, null=True)  # Field name made lowercase.
    step = models.BigIntegerField(db_column='Step', blank=True, null=True)  # Field name made lowercase.
    raw_step_id = models.BigIntegerField(db_column='Raw Step ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    start_voltage_v_field = models.FloatField(db_column='Start Voltage(V)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    end_voltage_v_field = models.FloatField(db_column='End Voltage(V)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    start_current_ma_field = models.FloatField(db_column='Start Current(mA)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    end_current_ma_field = models.FloatField(db_column='End Current(mA)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    capacity_mah_field = models.FloatField(db_column='CapaCity(mAh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    endure_time_h_min_s_ms_field = models.TextField(db_column='Endure Time(h:min:s.ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    relative_time_h_min_s_ms_field = models.TextField(db_column='Relative Time(h:min:s.ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    absolute_time = models.DateTimeField(db_column='Absolute Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    charge_capacity_mah_field = models.FloatField(db_column='Charge_Capacity(mAh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    discharge_capacity_mah_field = models.FloatField(db_column='Discharge_Capacity(mAh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    net_engy_dchg_mwh_field = models.FloatField(db_column='Net Engy_DChg(mWh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    engy_chg_mwh_field = models.FloatField(db_column='Engy_Chg(mWh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    engy_dchg_mwh_field = models.FloatField(db_column='Engy_DChg(mWh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = 'Statis_67_3_5'
