from django import forms
from core.models import SiteSetting, Advantage, News, ContactMessage
from services.models import Service, Order
from user.models import User

class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = '__all__'
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
            'mission': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class AdvantageForm(forms.ModelForm):
    class Meta:
        model = Advantage
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message', 'answer', 'status']
        widgets = {
            'message': forms.Textarea(attrs={'readonly': 'readonly', 'rows': 4}),
            'answer': forms.Textarea(attrs={'rows': 4}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'phone', 'address']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+7 XXX XXX-XX-XX'}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }