from django.contrib.auth.models import User

from .models import CarReview, Profilis, Order_line, Order
from django import forms

class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = ('content', 'car', 'reviewer')
        widgets = {'car': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['data', 'car', 'reader','due_back']

class OrderLineCreateForm(forms.ModelForm):
    class Meta:
        model = Order_line
        fields = ['service','order', 'quantity']

class CombinedOrderForm(forms.ModelForm):

    # Kopijuoti OrderLineCreateForm laukus
    service = forms.CharField()
    quantity = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['data', 'car', 'reader', 'due_back', 'service', 'quantity']


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['data', 'car', 'due_back', 'status']
