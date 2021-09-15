import os
from django.core.exceptions import ValidationError
from django.db import models
from multiselectfield import MultiSelectField

FREQUENCY = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)

LEVEL = (
    (1, 'Basic'),
    (2, 'Intermediate'),
    (3, 'Advance'),
)


def validate_img_file(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_pdf_file(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    print(ext)
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Workshop(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    hours = models.PositiveIntegerField()
    sessions = models.PositiveIntegerField()
    workshops = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    level = MultiSelectField(choices=LEVEL)
    frequency = MultiSelectField(choices=FREQUENCY)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    cover = models.ImageField(upload_to='poster', blank=True, validators=[validate_img_file])
    temary = models.FileField(upload_to='temary', blank=True, validators=[validate_pdf_file])
