from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('cart',views.show_cart,name='show_cart'),
    # path('list_products',views.list_products,name='list_products'),
    # path('detail_product',views.detail_product,name='detail_product'),
]
