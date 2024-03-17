from django.urls import path
from . import views 



urlpatterns = [
    path('product/create_bulk', views.bulk_create_products, name='bulk_create_products'),
    
]