from rest_framework import serializers
from ..models import Product ,Category,Cart,Cartitems

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category_id','title']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price','category','evaluation']
    
    category =CategorySerializer()        

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price']

class CartItemSerializer(serializers.ModelSerializer):
    product=SimpleProductSerializer( )
    sub_total=serializers.SerializerMethodField(method_name='total')
    class Meta:
        model=Cartitems
        fields=['id','cart','product','quantity','sub_total']

    def total (self,cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price
    
class CartSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    items=CartItemSerializer(many=True)
    grand_total=serializers.SerializerMethodField(method_name="main_total")
    class Meta:
        model=Cart
        fields=['id','items','grand_total']
    
    def main_total(self,cart:Cart):
        items=cart.items.all()
        total=sum([item.quantity * item.product.price for item in items])
        return total