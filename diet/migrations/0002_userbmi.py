# Generated by Django 3.2.9 on 2021-11-07 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umur', models.IntegerField()),
                ('tinggi_badan', models.FloatField()),
                ('berat_badan', models.FloatField()),
                ('jenis_kelamin', models.CharField(max_length=100)),
                ('tingkat_aktivitas', models.CharField(max_length=250)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
