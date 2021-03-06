# Generated by Django 3.2.9 on 2021-11-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_userbmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbmi',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userbmi',
            name='tingkat_aktivitas',
            field=models.CharField(choices=[('Sedantary', 'Sedentary: little or no exercise'), ('Exercise 1-3', 'Exercise 1-3 times/week'), ('Exercise 4-5', 'Exercise 4-5 times/week'), ('Daily', 'Daily exercise or intense exercise 3-4 times/week'), ('Intense', 'Intense exercise 6-7 times/week'), ('Very intense', 'Very intense exercise daily, or physical job')], max_length=250),
        ),
    ]
