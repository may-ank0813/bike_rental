from django import forms
from .models import Bike, Order, PrivateMsg

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = [
            "image",
            "bike_name",
            "company_name",
            "cost_par_day",
            "content",
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "bike_name",
            "employee_name",
            "cell_no",
            "address",
            "date",
            "to",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]