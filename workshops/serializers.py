from rest_framework import serializers

from workshops.models import Workshop


class WorkshopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'
