from django import forms

from main.models import contact as models

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        exclude = ["user",]
