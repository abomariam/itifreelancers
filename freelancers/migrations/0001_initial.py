# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('is_from_cs_background', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('hourly', 'Hourly'), ('fixed-price', 'Fixed Price')], max_length=150, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('applied_at', models.DateField(blank=True, null=True)),
                ('is_interviewed', models.NullBooleanField()),
                ('interviewed_at', models.DateField(blank=True, null=True)),
                ('interview_channel', models.CharField(blank=True, choices=[('chat', 'Text Chat'), ('voice', 'Voice Chat'), ('video', 'Video Chat')], max_length=150, null=True)),
                ('interview_notes', models.TextField(blank=True, null=True)),
                ('is_hired', models.NullBooleanField()),
                ('hired_at', models.DateField(blank=True, null=True)),
                ('hiring_notes', models.TextField(blank=True, null=True)),
                ('is_completed_successfully', models.NullBooleanField()),
                ('is_disputed', models.NullBooleanField()),
                ('dispute_notes', models.TextField(blank=True, null=True)),
                ('total_working_hours', models.IntegerField(blank=True, null=True)),
                ('total_job_income', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('closed_at', models.DateField(blank=True, null=True)),
                ('client_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelancers.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('site', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('status', models.CharField(choices=[('in-review', 'In Review'), ('approved', 'Approved'), ('suspended', 'Suspended')], default='in-review', max_length=50)),
                ('joined_at', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='freelancers.Freelancer')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='freelancers.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='working_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='freelancers.WorkingField'),
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='freelancers.Profile'),
        ),
        migrations.AddField(
            model_name='job',
            name='working_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='freelancers.WorkingField'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='Intake',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancers', to='freelancers.Intake'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freelancers', to='freelancers.City'),
        ),
    ]
