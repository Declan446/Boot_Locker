from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_boots, name='boots'),
    path('<int:boot_id>/', views.boot_detail, name='boot_detail'),
    path('add/', views.add_product, name='add_product'),
]
