from django.urls import path
from .views import index, basket

urlpatterns = [
    path('', index),
    path('/basket', basket)
]
