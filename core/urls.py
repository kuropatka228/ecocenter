from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('faq/<int:message_id>/', views.answer_faq, name='answer_faq'),

    path('news/<int:pk>/delete/', views.news_delete, name='admin_news_delete')
]