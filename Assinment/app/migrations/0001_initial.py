# Generated by Django 3.0.8 on 2020-07-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=10)),
                ('subject', models.CharField(blank=True, max_length=10)),
                ('memo', models.CharField(blank=True, max_length=50)),
                ('created_time', models.DateTimeField(blank=True, max_length=10)),
                ('hits', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
