from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from .models import MailList


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'base/index.html', {})


class MailListView(ListView):
    template_name = 'base/user-list.html'
    model = MailList
