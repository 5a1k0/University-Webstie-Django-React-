# Generated by Django 5.0.4 on 2024-09-20 00:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_studentdetails_enrollment_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('faculty_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
