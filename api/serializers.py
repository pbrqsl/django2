from rest_framework import serializers

from basket.models import Customer, Basket

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    basket = BasketSerializer(many=False)
    class Meta:
        model = Customer
        fields = '__all__'

