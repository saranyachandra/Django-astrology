# Generated by Django 3.2.5 on 2021-07-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='astro_details',
            name='exp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
