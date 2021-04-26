from rest_framework import serializers
from base.models import task

class dataserializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'
