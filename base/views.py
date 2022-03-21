import datetime

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import View, ListView, FormView

from .forms import MailListForm
from .models import MailList


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


class SendEmail(View):
    def get(self, request):
        subject, from_email, to_email = 'Hello', settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER
        text_message = render_to_string('email/message.html', {'username': 'Anuarcheck', 'date': datetime.datetime.now()})
        msg = EmailMultiAlternatives(subject, text_message, from_email, [to_email, ], )
        msg.send()

        # text_message = render_to_string(
        #     'account/managers/mail_manager/create_delivery_lot_order.html',
        #     dict(order=order, path_link='sold-orders', ))

        # send_mail('Greetings!', 'temp', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, ], )
        return redirect('index')
