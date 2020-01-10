from rest_framework import serializers
from .models import Visitor


class createVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['first_name', 'last_name', 'plate_number', 'reason']



class viewVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'


class UpdateVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['present']

