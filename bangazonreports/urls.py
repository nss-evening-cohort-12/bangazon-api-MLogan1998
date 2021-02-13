from django.urls import path
from .views import inexpensive_products, expensive_products

urlpatterns = [
    path('reports/inexpensive', inexpensive_products),
    path('reports/expensive', expensive_products)
]
