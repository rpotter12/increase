# Generated by Django 2.2.2 on 2019-06-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('ph', models.CharField(max_length=100)),
                ('email', models.EmailField(default='null', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]