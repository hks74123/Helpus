# Generated by Django 3.2.3 on 2021-05-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonal',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
        migrations.AddField(
            model_name='userpersonal',
            name='unicode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
