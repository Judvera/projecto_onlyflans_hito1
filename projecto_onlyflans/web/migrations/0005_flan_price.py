# Generated by Django 4.2.11 on 2024-04-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='Precio'),
        ),
    ]
