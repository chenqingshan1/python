# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-06 03:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170405_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_customer_list', '\u67e5\u770b\u5ba2\u6237\u5217\u8868'), ('view_customer_info', '\u67e5\u770b\u5ba2\u6237\u8be6\u60c5'), ('edit_own_customer_info', '\u4fee\u6539\u81ea\u5df1\u7684\u5ba2\u6237\u4fe1\u606f'))},
        ),
    ]
