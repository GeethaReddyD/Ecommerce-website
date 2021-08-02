# Generated by Django 3.2.4 on 2021-08-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eproject', '0002_auto_20210718_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('emailId', models.CharField(max_length=50)),
                ('phoneNo', models.IntegerField()),
                ('price', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]