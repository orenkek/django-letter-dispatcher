from django.urls import path
from base.views import Index

urlpatterns = [
   path('', Index.as_view()),
]
