# Generated by Django 2.1 on 2018-08-28 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('activities', 'Lobby Activities'), ('registrations', 'Lobby Registrations')], max_length=20)),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('interest', models.CharField(blank=True, max_length=250, null=True)),
                ('bill', models.CharField(blank=True, max_length=250, null=True)),
                ('start', models.CharField(blank=True, max_length=50, null=True)),
                ('end', models.CharField(blank=True, max_length=50, null=True)),
                ('session', models.CharField(blank=True, max_length=10, null=True)),
                ('latest_only', models.BooleanField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
