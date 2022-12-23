from django.urls import path
from .views import GetFoods

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('foods', GetFoods, basename='foods')
# urlpatterns = router.urls


urlpatterns = [
    path('foods',GetFoods.as_view(),name='foods'),
]
