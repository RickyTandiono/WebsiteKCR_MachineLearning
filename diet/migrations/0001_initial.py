# Generated by Django 3.2.9 on 2021-11-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('protein', models.FloatField()),
                ('lemak', models.FloatField()),
                ('karbo', models.FloatField()),
                ('kalori', models.FloatField()),
                ('jenis', models.CharField(max_length=250)),
            ],
        ),
    ]
