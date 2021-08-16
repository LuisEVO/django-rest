# Generated by Django 3.2.4 on 2021-08-11 22:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20210811_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='frequency',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='level',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Basic'), (2, 'Intermediate'), (3, 'Advance')], default=1, max_length=5, null=True),
        ),
    ]
