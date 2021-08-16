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
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Workshop(models.Model):
    level = MultiSelectField(choices=LEVEL, blank=True, null=True)
    frequency = MultiSelectField(choices=FREQUENCY, blank=True, null=True)
    # name = models.CharField(max_length=50)
    # description = models.CharField(max_length=250)
    # price =
    # start_date =
    # start_time =
    # end_time =
    cover = models.ImageField(upload_to='poster', blank=True, validators=[validate_img_file])
    temary = models.ImageField(upload_to='temary', blank=True, validators=[validate_pdf_file])
