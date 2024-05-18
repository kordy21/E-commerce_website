from rest_framework import serializers
from product.models import Products ,Category

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name','discount','old_price','category','evaluation']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'