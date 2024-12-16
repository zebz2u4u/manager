# Generated by Django 5.1.4 on 2024-12-16 20:05

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255, verbose_name='Full Name')),
                ('workEmail', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Email must be a valid email address ending with @arm.com.', regex='^[a-zA-Z0-9_.+-]+@arm\\.com$')], verbose_name='Work Email')),
                ('lineManager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='line_managed', to='manager_webapp.employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('request', models.CharField(max_length=550)),
                ('request_type', models.CharField(choices=[('DeviceRequest', 'Device Request'), ('MaintenanceRequest', 'Maintenance Request'), ('OtherRequest', 'Other')], max_length=20, verbose_name='Request Type')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='manager_webapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='RequestUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('update_text', models.TextField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='manager_webapp.request')),
            ],
        ),
    ]