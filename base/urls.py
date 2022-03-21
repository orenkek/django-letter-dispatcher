from django.urls import path
from base.views import Index, MailListView, MailListFormView, SendEmail

urlpatterns = [
   path('', Index.as_view(), name='index'),
   path('mail-list/', MailListView.as_view(), name='mail_list'),
   path('mail-list/create', MailListFormView.as_view(), name='mail_list_create'),
   path('send-mail/', SendEmail.as_view(), name='send_mail')
]
