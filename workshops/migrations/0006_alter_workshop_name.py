# Generated by Django 3.2.4 on 2021-09-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0005_alter_workshop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='name',
            field=models.TextField(max_length=250),
        ),
    ]
