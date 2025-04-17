from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404

def home(request):
    settings = SiteSetting.objects.first()
    advantages = Advantage.objects.all()
    news = News.objects.filter(is_active=True).order_by('-created_at')[:5]

    context = {
        'settings': settings,
        'advantages': advantages,
        'news': news,
    }
    return render(request, 'core/home.html', context)


def about(request):
    settings = SiteSetting.objects.first()
    return render(request, 'core/about.html', {'settings': settings})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.user = request.user
            message.save()
            messages.success(request, 'Ваше сообщение отправлено! Ответ появится на странице вопросов-ответов.')
            return redirect('faq')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})


def faq(request):
    if request.user.is_staff:
        messages = ContactMessage.objects.all().order_by('-created_at')
    else:
        messages = ContactMessage.objects.filter(status='published').order_by('-created_at')
    return render(request, 'core/faq.html', {'messages': messages})


@user_passes_test(lambda u: u.is_staff)
def answer_faq(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            message.delete()
            return redirect('faq')

        answer = request.POST.get('answer')
        status = request.POST.get('status', 'new')

        message.answer = answer
        message.status = status
        message.save()
        return redirect('faq')

    return render(request, 'core/answer_faq.html', {'message': message})


@login_required
def answer_message(request, message_id):
    if not request.user.is_staff:
        return redirect('home')

    message = ContactMessage.objects.get(id=message_id)

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer:
            message.answer = answer
            message.status = 'published'
            message.save()
            messages.success(request, 'Ответ успешно сохранен и опубликован!')
            return redirect('faq')

    return render(request, 'core/answer_message.html', {'message': message})

