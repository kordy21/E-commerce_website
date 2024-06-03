from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import ProductsSerializer ,CategorySerializer
from product.models import Products ,Category
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response 
# from rest_framework import status

class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class= ProductsSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer





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