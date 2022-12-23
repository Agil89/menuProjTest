from django.contrib import admin
from .models import FoodCategory, Food, Topping
# Register your models here.

admin.site.register(FoodCategory)

class ToppingAdminInline(admin.TabularInline):
    model = Topping
    min_num = 0
    extra = 0

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [ToppingAdminInline, ]