from .models import Food, FoodCategory
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.



class GetFoods(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(is_publish=True).all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('foods__is_publish','foods__is_vegan','foods__name')
    search_fields = ('is_publish','foods__is_vegan','foods__name')

    def list(self, request ):
        queryset = self.get_queryset()
        filters_backends = self.filter_queryset(queryset)
        serializer = CategorySerializer(filters_backends, many=True)
        return Response(serializer.data)

        

