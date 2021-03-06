# Generated by Django 2.0.7 on 2018-07-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AB', 'Assembly Bill'), ('SB', 'Senate Bill'), ('ACA', 'Assembly Constitutional Amendment'), ('SCA', 'Senate Constitutional Amendment'), ('AJR', 'Assembly Joint Resolution'), ('SJR', 'Senate Joint Resolution'), ('ACR', 'Assembly Concurrent Resolution'), ('SCR', 'Senate Concurrent Resolution'), ('HR', 'House Resolution'), ('SR', 'Senate Resolution')], max_length=3)),
                ('number', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('full_name', models.CharField(blank=True, max_length=300, null=True)),
                ('authors', models.CharField(blank=True, max_length=250, null=True)),
                ('coauthors', models.CharField(blank=True, max_length=250, null=True)),
                ('sections', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('digest', models.TextField(blank=True, null=True)),
                ('analysis', models.TextField(blank=True, null=True)),
                ('introduction_date', models.DateField(blank=True, null=True)),
                ('session', models.CharField(choices=[('20172018', '2017 - 2018')], max_length=8)),
            ],
        ),
    ]
