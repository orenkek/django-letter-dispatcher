from django.forms import ModelForm
from .models import MailList


class MailListForm(ModelForm):
    class Meta:
        model = MailList
        fields = ['name', 'email', ]
