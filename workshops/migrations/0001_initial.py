# Generated by Django 3.2.4 on 2021-09-05 04:04

from django.db import migrations, models
import multiselectfield.db.fields
import workshops.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Basic'), (2, 'Intermediate'), (3, 'Advance')], max_length=5, null=True)),
                ('frequency', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=13, null=True)),
                ('name', models.TextField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, upload_to='poster', validators=[workshops.models.validate_img_file])),
                ('temary', models.ImageField(blank=True, upload_to='temary', validators=[workshops.models.validate_pdf_file])),
            ],
        ),
    ]
