from rest_framework import serializers
from .models import (
    Review,
)

# serializer class
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'