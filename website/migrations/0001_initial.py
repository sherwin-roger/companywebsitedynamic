# Generated by Django 3.1.1 on 2021-01-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peoplename', models.CharField(max_length=100)),
                ('itemname', models.CharField(max_length=100)),
                ('itemprice', models.IntegerField()),
            ],
        ),
    ]
