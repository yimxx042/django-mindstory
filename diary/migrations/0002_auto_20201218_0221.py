# Generated by Django 2.2 on 2020-12-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='dt_created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='page',
            name='dt_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
