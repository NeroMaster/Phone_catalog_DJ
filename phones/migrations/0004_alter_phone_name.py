# Generated by Django 4.2.3 on 2023-07-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Модель'),
        ),
    ]
