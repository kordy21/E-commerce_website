from django.shortcuts import render
from .serializers import ProductsSerializer ,CategorySerializer,CartSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin ,DestroyModelMixin,RetrieveModelMixin

from ..models import Product,Category,Cart
from .filters import ProductFilter


# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response 
# from rest_framework import status

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductsSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class=ProductFilter
    search_fields=['name']
    ordering_fields=['old_price']
    lookup_field='slug'
    pagination_class=PageNumberPagination
    
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer
    lookup_field='slug'

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class= CartSerializer



# @api_view(['GET','POST'])
# def api_products(request):
#     if request.method=='GET':
#         products=Products.objects.all()
#         serializer=ProductsSerializer(products,many=True)
#         return Response(serializer.data)
    
#     elif request.method =='POST':
#         serializer=ProductsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['GET','PUT','DELETE'])
# def api_product(request,pk):
#     product=get_object_or_404(Products,id=pk)
#     if request.method =='GET':
#         # product=Products.objects.get(id=pk)
#         serializer=ProductsSerializer(product)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer=ProductsSerializer(product,data=request.data)
#         serializer.is_vaild(raise_excaption=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method =='DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view()
# def api_categories(request):
#     categories=Category.objects.all()
#     serializer=CategorySerializer(categories,many=True)
#     return Response(serializer.data)

# @api_view()
# def api_category(request,pk):
#     category=get_object_or_404(Category,category_id=pk)
#     # product=Products.objects.get(id=pk)
#     serializer=CategorySerializer(category)
#     return Response(serializer.data)