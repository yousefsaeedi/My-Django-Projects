from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['count', 'served']
        context_object_name = 'form'
        template_name = 'base/create_order.html'

class OrderUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'count', 'served']
        context_object_name = 'form'
        template_name = 'base/update_order.html'