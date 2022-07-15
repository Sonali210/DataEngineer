# Generated by Django 4.0.6 on 2022-07-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle6731',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.BigIntegerField(blank=True, null=True)),
                ('total_of_cycle', models.BigIntegerField(blank=True, null=True)),
                ('capacity_of_charge_mah_field', models.FloatField(blank=True, null=True)),
                ('capacity_of_discharge_mah_field', models.FloatField(blank=True, null=True)),
                ('cycle_life_field', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle6735',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.BigIntegerField(blank=True, null=True)),
                ('total_of_cycle', models.BigIntegerField(blank=True, null=True)),
                ('capacity_of_charge_mah_field', models.FloatField(blank=True, null=True)),
                ('capacity_of_discharge_mah_field', models.FloatField(blank=True, null=True)),
                ('cycle_life_field', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail6731',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_index', models.BigIntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('jumpto', models.BigIntegerField(blank=True, null=True)),
                ('cycle', models.BigIntegerField(blank=True, null=True)),
                ('step', models.BigIntegerField(blank=True, null=True)),
                ('cur_ma_field', models.FloatField(blank=True, null=True)),
                ('voltage_v_field', models.FloatField(blank=True, null=True)),
                ('capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('energy_mwh_field', models.FloatField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('absolute_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail6735',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_index', models.BigIntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('jumpto', models.BigIntegerField(blank=True, null=True)),
                ('cycle', models.BigIntegerField(blank=True, null=True)),
                ('step', models.BigIntegerField(blank=True, null=True)),
                ('cur_ma_field', models.FloatField(blank=True, null=True)),
                ('voltage_v_field', models.FloatField(blank=True, null=True)),
                ('capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('energy_mwh_field', models.FloatField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('absolute_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detailtemp6731',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.BigIntegerField(blank=True, null=True)),
                ('step_name', models.TextField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('realtime', models.DateTimeField(blank=True, null=True)),
                ('auxiliary_channel_tu1_t_c_field', models.FloatField(blank=True, null=True)),
                ('gap_of_temperature', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detailtemp6735',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.BigIntegerField(blank=True, null=True)),
                ('step_name', models.TextField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('realtime', models.DateTimeField(blank=True, null=True)),
                ('auxiliary_channel_tu1_t_c_field', models.FloatField(blank=True, null=True)),
                ('gap_of_temperature', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detailvol6731',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.BigIntegerField(blank=True, null=True)),
                ('step_name', models.TextField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('realtime', models.DateTimeField(blank=True, null=True)),
                ('auxiliary_channel_tu1_u_v_field', models.FloatField(blank=True, null=True)),
                ('gap_of_voltage', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detailvol6735',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.BigIntegerField(blank=True, null=True)),
                ('step_name', models.TextField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('realtime', models.DateTimeField(blank=True, null=True)),
                ('auxiliary_channel_tu1_u_v_field', models.FloatField(blank=True, null=True)),
                ('gap_of_voltage', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statis6731',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.BigIntegerField(blank=True, null=True)),
                ('cycle', models.BigIntegerField(blank=True, null=True)),
                ('step', models.BigIntegerField(blank=True, null=True)),
                ('raw_step_id', models.BigIntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('start_voltage_v_field', models.FloatField(blank=True, null=True)),
                ('end_voltage_v_field', models.FloatField(blank=True, null=True)),
                ('start_current_ma_field', models.FloatField(blank=True, null=True)),
                ('end_current_ma_field', models.FloatField(blank=True, null=True)),
                ('capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('endure_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('absolute_time', models.DateTimeField(blank=True, null=True)),
                ('discharge_capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('charge_capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('discharge_capacity_mah_1', models.FloatField(blank=True, null=True)),
                ('net_engy_dchg_mwh_field', models.FloatField(blank=True, null=True)),
                ('engy_chg_mwh_field', models.FloatField(blank=True, null=True)),
                ('engy_dchg_mwh_field', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statis6735',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.BigIntegerField(blank=True, null=True)),
                ('cycle', models.BigIntegerField(blank=True, null=True)),
                ('step', models.BigIntegerField(blank=True, null=True)),
                ('raw_step_id', models.BigIntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('start_voltage_v_field', models.FloatField(blank=True, null=True)),
                ('end_voltage_v_field', models.FloatField(blank=True, null=True)),
                ('start_current_ma_field', models.FloatField(blank=True, null=True)),
                ('end_current_ma_field', models.FloatField(blank=True, null=True)),
                ('capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('endure_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('relative_time_h_min_s_ms_field', models.TextField(blank=True, null=True)),
                ('absolute_time', models.DateTimeField(blank=True, null=True)),
                ('charge_capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('discharge_capacity_mah_field', models.FloatField(blank=True, null=True)),
                ('net_engy_dchg_mwh_field', models.FloatField(blank=True, null=True)),
                ('engy_chg_mwh_field', models.FloatField(blank=True, null=True)),
                ('engy_dchg_mwh_field', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
