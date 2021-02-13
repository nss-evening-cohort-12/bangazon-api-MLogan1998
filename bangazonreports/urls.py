from django.urls import path
from .views import inexpensive_products

urlpatterns = [
    path('reports/inexpensive', inexpensive_products)
]
