from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import RegisterSerializer, ProductSerializer

# Create your views here.

class RegisterView(APIView):
    register=RegisterSerializer
    def get(self,request):
        reg=Registration.objects.all().values()
        return Response({'Register':reg})
    
    def post(self,request):
        reg=RegisterSerializer(data=request.data)

        if reg.is_valid():
            reg.save()
            return Response({"Data saved":reg.data})
        else:
            return Response({"Invalid Data"})

class ProductView(APIView):
    product=ProductSerializer
    def get(self, request):
        prod=ProductDetails.objects.all().values()
        return Response({'Products':'details','details':prod})
    
    def post(self,request):
        prod=ProductSerializer(data=request.data)
        if prod.is_valid():
            prod.save()
            return Response({'products':prod.data})
        else:
            return Response({'Invalid data'})

    
class Filter(APIView):
    def company_detail(self,company_name):
        try:
            compy=Registration.objects.get(companyName=company_name)
            return {
                'company Name':compy
            }
        except Registration.DoesNotExist:
            return Response({'company name not found'})
        
    def product_detail(self,company_name):
        try:
            prod=ProductDetails.objects.get(companyName=company_name)
            return {
                "companyName": prod.companyName,
                "productName": prod.productName,
                "price": prod.price,
                "rating": prod.rating,
                "discount": prod.discount,
                "availability": prod.availability
            }
        except ProductDetails.DoesNotExist:
            return Response({"Not prodcut list"})
        

    def get(self,request,company_name):
        compy=self.company_detail(company_name)
        if compy:
            prod_det=self.product_detail(company_name)
            if prod_det:
                return Response({
                'company_name':company_name,
                'product_detail':prod_det
            })
            else:
                return Response({'Error':'No prod found'})
        else:
            return Response({'Error':'No company found'})
