from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetails
        fields='__all__'

