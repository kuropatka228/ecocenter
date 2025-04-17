from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Order
from .forms import OrderForm
from django.contrib import messages


def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})


@login_required
def create_order(request, service_id):
    service = Service.objects.get(pk=service_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.service = service
            order.save()
            messages.success(request, 'Ваша заявка успешно создана!')
            return redirect('my_orders')
    else:
        form = OrderForm(initial={'service': service})

    return render(request, 'services/create_order.html', {'form': form, 'service': service})


@login_required
def my_orders(request):
    if request.method == 'POST' and request.user.is_staff:
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        try:
            order = Order.objects.get(id=order_id)
            if new_status in dict(Order.STATUS_CHOICES).keys():
                order.status = new_status
                order.save()
                messages.success(request, 'Статус заявки успешно обновлен!')
        except Order.DoesNotExist:
            messages.error(request, 'Заявка не найдена!')
        return redirect('my_orders')

    if request.user.is_staff:
        orders = Order.objects.all().order_by('-created_at')
    else:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'services/order_list.html', {'orders': orders})