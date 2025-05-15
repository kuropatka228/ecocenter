from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from core.models import SiteSetting, Advantage, News, ContactMessage, Advantage
from services.models import Service, Order
from user.models import User
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SiteSettingForm, AdvantageForm, NewsForm, ContactMessageForm, ServiceForm, OrderForm, UserForm

def staff_required(view_func):
    return user_passes_test(lambda u: u.is_staff)(view_func)

# Dashboard
@staff_required
def admin_dashboard(request):
    stats = {
        'user': User.objects.count(),
        'order': Order.objects.count(),
        'contactmessage': ContactMessage.objects.count(),
        'news': News.objects.count(),
    }
    return render(request, 'admin/dashboard.html', {'stats': stats})


# SiteSetting
@staff_required
def site_setting_list(request):
    setting = SiteSetting.objects.first()
    return render(request, 'admin/sitesetting/list.html', {'setting': setting})


@staff_required
def site_setting_edit(request, pk=None):
    instance = get_object_or_404(SiteSetting, pk=pk) if pk else None
    if request.method == 'POST':
        form = SiteSettingForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_sitesetting_list')
    else:
        form = SiteSettingForm(instance=instance)
    return render(request, 'admin/sitesetting/form.html', {'form': form})


# News
@staff_required
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'admin/news/list.html', {'news': news})


@staff_required
def news_edit(request, pk=None):
    instance = get_object_or_404(News, pk=pk) if pk else None
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_news_list')
    else:
        form = NewsForm(instance=instance)
    return render(request, 'admin/news/form.html', {'form': form})


# Advantage
@staff_required
def advantage_list(request):
    advantages = Advantage.objects.all()
    return render(request, 'admin/advantage/list.html', {'advantages': advantages})


@staff_required
def advantage_edit(request, pk=None):
    instance = get_object_or_404(Advantage, pk=pk) if pk else None
    if request.method == 'POST':
        form = AdvantageForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_advantage_list')
    else:
        form = AdvantageForm(instance=instance)
    return render(request, 'admin/advantage/form.html', {'form': form})

@staff_member_required
def advantage_delete(request, pk):
    advantage = get_object_or_404(Advantage, pk=pk)
    advantage.delete()
    messages.success(request, "Преимущество удалено.")
    return redirect('admin_advantage_list')


# ContactMessage
@staff_required
def contact_message_list(request):
    status_filter = request.GET.get('status', 'all')
    messages = ContactMessage.objects.all().order_by('-created_at')

    if status_filter != 'all':
        messages = messages.filter(status=status_filter)

    return render(request, 'admin/contactmessage/list.html', {
        'contactmessage': messages,
        'status_filter': status_filter,
        'status_choices': ContactMessage.STATUS_CHOICES
    })


@staff_required
def contact_message_edit(request, pk):
    instance = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        if 'delete' in request.POST:
            instance.delete()
            return redirect('admin_contactmessage_list')  # Или куда тебе нужно
        form = ContactMessageForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_contactmessage_list')  # Или обратно к списку
    else:
        form = ContactMessageForm(instance=instance)
    return render(request, 'admin/contactmessage/form.html', {'form': form})


@staff_member_required
def contactmessage_delete(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    message.delete()
    messages.success(request, "Сообщение удалено.")
    return redirect('admin_contactmessage_list')

# Service
@staff_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin/service/list.html', {'services': services})


@staff_required
def service_edit(request, pk=None):
    instance = get_object_or_404(Service, pk=pk) if pk else None
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_service_list')
    else:
        form = ServiceForm(instance=instance)
    return render(request, 'admin/service/form.html', {'form': form})

@staff_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('admin_service_list')


# Order
@staff_required
def order_list(request):
    status_filter = request.GET.get('status', 'all')
    orders = Order.objects.all().order_by('-created_at')

    if status_filter != 'all':
        orders = orders.filter(status=status_filter)

    return render(request, 'admin/order/list.html', {
        'order_list': orders,
        'status_filter': status_filter,
        'status_choices': Order.STATUS_CHOICES
    })


@staff_required
def order_edit(request, pk=None):
    instance = get_object_or_404(Order, pk=pk) if pk else None
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_order_list')
    else:
        form = OrderForm(instance=instance)
    return render(request, 'admin/order/form.html', {'form': form})


@staff_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('admin_order_list')


# User
@staff_required
def user_list(request):
    users = User.objects.all()  # получить всех пользователей
    return render(request, 'admin/user/list.html', {'users': users})


@staff_required
def user_edit(request, pk=None):
    instance = get_object_or_404(User, pk=pk) if pk else None
    if request.method == 'POST':
        form = UserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin_user_list')
    else:
        form = UserForm(instance=instance)
    return render(request, 'admin/user/form.html', {'form': form})