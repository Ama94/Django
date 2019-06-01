from django import forms

class ProductForm(forms.Form):
    price = forms.FloatField(label="Price")
    name = forms.CharField(label="Name")
    description = forms.CharField(label="Description", widget=forms.Textarea)