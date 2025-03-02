from rest_framework import serializers
from .models import ModelTask


class SerializersTask(serializers.ModelSerializer):
    class Meta:
        model = ModelTask
        fields = '__all__'

