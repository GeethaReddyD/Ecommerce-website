# Generated by Django 3.2.4 on 2021-08-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eproject', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='welcome', max_length=20),
        ),
    ]
