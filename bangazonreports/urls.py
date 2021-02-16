from django.urls import path
from .views import inexpensive_products, expensive_products, completed_orders, incomplete_orders, favorite_sellers

urlpatterns = [
    path('reports/inexpensive', inexpensive_products),
    path('reports/expensive', expensive_products),
    path('reports/completed', completed_orders),
    path('reports/incomplete', incomplete_orders),
    path('reports/favorites', favorite_sellers),
]
