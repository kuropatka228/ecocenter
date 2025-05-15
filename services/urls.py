from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
    path('<int:service_id>/order/', views.create_order, name='create_order'),
    path('my-order/', views.my_orders, name='my_orders'),
]