from django import forms

from .models import Order, Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'quantity'
        ]


    # def clean_quantity(self):
    #     quantity=self.cleaned_data.get('quantity')
    #     product_quantity=Product.objects.get(title=product)
    #     if quantity>product_quantity.quantity:
    #         raise forms.ValidationError("Siz soragan miqdordan kam")
    #     return quantity
