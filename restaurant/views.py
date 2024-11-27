from django.db.models import Prefetch, Count, Q
from rest_framework.generics import ListAPIView
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodsView(ListAPIView):

    queryset = (FoodCategory.objects.prefetch_related(
        Prefetch('food', queryset=Food.objects.filter(is_publish=True)), 'food__additional')
                .annotate(foods=Count('food', filter=Q(food__is_publish=False)))
                .exclude(foods=Count('food__is_publish')))

    serializer_class = FoodListSerializer
