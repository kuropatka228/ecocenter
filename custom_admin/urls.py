from django.urls import path
from . import views
from .views import contact_message_edit
urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),

    # SiteSetting
    path('site-settings/', views.site_setting_list, name='admin_sitesetting_list'),
    path('site-settings/<int:pk>/', views.site_setting_edit, name='admin_sitesetting_edit'),

    # News
    path('news/', views.news_list, name='admin_news_list'),
    path('news/<int:pk>/', views.news_edit, name='admin_news_edit'),
    path('news/new/', views.news_edit, name='admin_news_create'),

    # Advantage
    path('advantages/', views.advantage_list, name='admin_advantage_list'),
    path('advantages/<int:pk>/', views.advantage_edit, name='admin_advantage_edit'),
    path('advantages/new/', views.advantage_edit, name='admin_advantage_create'),
    path('advantages/<int:pk>/delete/', views.advantage_delete, name='admin_advantage_delete'),

    # ContactMessage
    path('contactmessage/', views.contact_message_list, name='admin_contactmessage_list'),
    path('contactmessage/<int:pk>/', views.contact_message_edit, name='admin_contactmessage_edit'),
    path('contact-messages/<int:pk>/edit/', contact_message_edit, name='answer_faq'),
    path('contact-messages/<int:pk>/delete/', views.contactmessage_delete, name='admin_contactmessage_delete'),

    # Service
    path('service/', views.service_list, name='admin_service_list'),
    path('service/<int:pk>/', views.service_edit, name='admin_service_edit'),
    path('service/new/', views.service_edit, name='admin_service_create'),
    path('service/delete/<int:pk>/', views.service_delete, name='admin_service_delete'),


    # Order
    path('order/', views.order_list, name='admin_order_list'),
    path('order/<int:pk>/', views.order_edit, name='admin_order_edit'),
    path('order/delete/<int:pk>/', views.order_delete, name='admin_order_delete'),

    # User
    path('user/', views.user_list, name='admin_user_list'),
    path('user/<int:pk>/', views.user_edit, name='admin_user_edit'),
]