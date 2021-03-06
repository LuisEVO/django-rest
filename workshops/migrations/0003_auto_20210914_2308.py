# Generated by Django 3.2.4 on 2021-09-15 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_alter_workshop_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='hours',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='sessions',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
