from rest_framework import serializers
from Product.models import Product  # Change this line

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

