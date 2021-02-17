  
from rest_framework import viewsets
from bangazonapi.models import ProductRating
from rest_framework import serializers

class RatingsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductRating
        fields = ('id', 'rating', 'product', 'customer')
        
class RatingVIewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = RatingsSerializer
