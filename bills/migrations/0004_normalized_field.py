# Generated by Django 2.0.7 on 2018-07-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_allow_null_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='normalized',
            field=models.BooleanField(default=False),
        ),
    ]
