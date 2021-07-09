# Generated by Django 3.2 on 2021-07-09 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagementapp', '0005_auto_20210709_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermedicine',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='ordermedicine',
            name='med_name',
            field=models.ManyToManyField(default=0, to='HospitalManagementapp.MedicalStore'),
        ),
        migrations.AlterField(
            model_name='ordermedicine',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 20, 15, 34, 525606)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 20, 15, 34, 506655)),
        ),
    ]
