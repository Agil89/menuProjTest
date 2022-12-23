from django.test import TestCase
from menu_app.models import *
from rest_framework.test import APIRequestFactory
from django.test import Client


class AnimalTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get('/menu/foods')
        factory = APIRequestFactory()
        self.request = factory.get('/menu/foods')

    def create_data(self):
        cat1 = FoodCategory.objects.create(name="cat1", is_publish=True)
        food1 = Food.objects.create(name="food1", description="desc1",category=cat1,price='11',is_special=True,is_vegan=True,is_publish=True)
        topping1 = Topping.objects.create(food=food1,name='topping1')
        

    def test_response_object(self):
        self.create_data()
        c = Client()
        response = c.get('/menu/foods').json()
        data = [{'id': 1, 'name': 'cat1', 'foods':
         [{'name': 'food1', 'description': 'desc1', 'price': 11, 'is_special': True, 'is_vegan': True, 'is_publish': True,
          'toppings': ['topping1']}]}]
        self.assertEqual(data, response)

    def test_food_is_publish_false(self):
        self.create_data()
        c = Client()
        response = c.get('/menu/foods?foods__is_publish=false').json()
        data = []
        self.assertEqual(data, response)
    
    def test_food_is_publish_true(self):
        self.create_data()
        c = Client()
        response = c.get('/menu/foods?foods__is_publish=true').json()
        data = [{'id': 1, 'name': 'cat1', 'foods':
         [{'name': 'food1', 'description': 'desc1', 'price': 11, 'is_special': True, 'is_vegan': True, 'is_publish': True,
          'toppings': ['topping1']}]}]
        self.assertEqual(data, response)
