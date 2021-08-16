from django.contrib import admin

# Register your models here.
from workshops.models import Workshop


class WorkshopAdmin(admin.ModelAdmin):
    fields = ['frequency']


admin.site.register(Workshop, WorkshopAdmin)
