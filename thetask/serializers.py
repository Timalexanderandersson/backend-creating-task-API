from rest_framework import serializers
from .models import ModelTask


class SerializersTask(serializers.ModelSerializer):
    class Meta:
        model = ModelTask
        fields = '__all__'
        extra_kwargs = {'user':{'read_only':True}}

