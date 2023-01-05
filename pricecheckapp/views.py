from django.shortcuts import render
from . models import Product 
from .serializers import Productserializer
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters





class ProductsAPIView(generics.ListCreateAPIView):
    search_fields = ['model_number']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    
    serializer_class=Productserializer
    
    def create(self , request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        else:
            return Response({"errors": serializer.errors})
