from rest_framework import serializers

from workshops.models import Workshop, LEVEL, FREQUENCY


class WorkshopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'

    frequency = serializers.MultipleChoiceField(choices=FREQUENCY, allow_blank=True, allow_null=True, required=False)
    level = serializers.MultipleChoiceField(choices=LEVEL, allow_blank=True, allow_null=True, required=False)


class WorkshopCoverPageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['cover']


class WorkshopTemaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['temary']
