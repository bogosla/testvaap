from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product', views.add_product, name='add_product'),
    path('edit_product', views.edit_product, name='edit_product'),
    path('product/<str:product_id>', views.product, name='product'),
    path('delete_product/<str:product_id>', views.delete_product, name='delete_product'),
]