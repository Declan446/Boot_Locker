from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_boots, name='boots'),
    path('<int:boot_id>/', views.boot_detail, name='boot_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('<int:boot_id>/addreview/', views.addreview, name='addreview'),
]
