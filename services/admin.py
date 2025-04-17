from django.contrib import admin
from .models import Service, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'service__title')
    list_editable = ('status',)