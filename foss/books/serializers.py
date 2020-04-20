from rest_framework import serializers
from .models import contributor

class contributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = contributor
        fields = ['foss', 'payment']