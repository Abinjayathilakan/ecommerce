from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('list_products',views.list_products,name='list_products'),
    path('product_details/<pk>',views.detail_product,name='detail_product'),
]
