# Generated by Django 3.1.7 on 2022-12-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('cId', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('cName', models.CharField(max_length=20)),
                ('cSex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('cBirthday', models.DateField()),
                ('cEmail', models.EmailField(blank=True, default='', max_length=100)),
                ('cPhone', models.CharField(blank=True, default='', max_length=50)),
                ('cAdd', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Mon.', 'Monday'), ('Tue.', 'Tuesday'), ('Wed.', 'Wednesday'), ('Thu.', 'Thursday'), ('Fri.', 'Friday'), ('Sat.', 'Saturday '), ('Sun.', 'Sunday')], max_length=15)),
                ('time', models.CharField(choices=[('1', '8:10-9:00'), ('2', '9:10-10:00'), ('3', '10:20-11:10'), ('4', '11:20-12:10'), ('5', '12:20-13:10'), ('6', '13:20-14:10'), ('7', '14:20-15:10'), ('8', '15:30-16:20'), ('9', '16:30-17:20'), ('10', '17:30-18:20')], max_length=15)),
            ],
        ),
    ]
