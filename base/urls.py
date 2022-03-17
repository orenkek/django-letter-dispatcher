from django.urls import path
from base.views import Index, MailListView, MailListFormView

urlpatterns = [
   path('', Index.as_view(), name='index'),
   path('mail-list/', MailListView.as_view(), name='mail_list'),
   path('mail-list/create', MailListFormView.as_view(), name='mail_list_create'),
]
