# Generated by Django 5.0.6 on 2024-08-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.CharField(max_length=100)),
                ('op2', models.CharField(max_length=100)),
                ('op3', models.CharField(max_length=100)),
                ('op1c', models.IntegerField(default=0)),
                ('op2c', models.IntegerField(default=0)),
                ('op3c', models.IntegerField(default=0)),
            ],
        ),
    ]
