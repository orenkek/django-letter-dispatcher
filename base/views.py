from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, FormView
from .models import MailList
from .forms import MailListForm


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'base/index.html', {})


class MailListView(ListView):
    template_name = 'base/user-list.html'
    model = MailList


class MailListFormView(FormView):
    template_name = 'base/mail-list-create.html'
    form_class = MailListForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
