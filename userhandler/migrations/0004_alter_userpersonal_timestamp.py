# Generated by Django 3.2.3 on 2021-05-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhandler', '0003_userpersonal_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
