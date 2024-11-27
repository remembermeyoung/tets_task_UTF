from django.urls import path
from .views import FoodsView

urlpatterns = [
    path('foods/', FoodsView.as_view()),
]