from rest_framework import serializers
from .models import OrderHistory, UserData
from .models import Product

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['username', 'password', 'mobno']

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'

class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model=OrderHistory
        fields = '__all__'