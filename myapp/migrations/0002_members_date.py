# Generated by Django 4.1 on 2022-09-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
