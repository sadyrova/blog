from django import forms


class TovarCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=2, max_length=254)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()
    quantity = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    comment = forms.CharField(min_length=2, max_length=254)
