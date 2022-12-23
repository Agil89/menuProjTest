from rest_framework import serializers
from .models import Food, FoodCategory, Topping



class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = ['name',]

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    toppings = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'is_special', 'is_vegan', 'is_publish', 'toppings']
        depth = 1

    
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    foods = FoodSerializer(read_only=True, many=True)
    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'foods']