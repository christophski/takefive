# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0034_auto_20171003_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name=b'The email address which will be displayed to the public'),
        ),
        migrations.AddField(
            model_name='venue',
            name='stripepubkey',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='stripesecretkey',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='reference',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='background',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name=b'Background for public pages such as guestlist sign up'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='logo',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name=b'Venue logo'),
        ),
    ]
