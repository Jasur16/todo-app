from rest_framework import serializers
from .models import TodoAppModel


class TodoModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = TodoAppModel
        fields = '__all__'