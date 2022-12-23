from django.db import models

# Create your models here.


class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods')
    price = models.PositiveIntegerField(default=0)
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Topping(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True, blank=True, related_name='toppings')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
