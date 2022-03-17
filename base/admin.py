from django.contrib import admin

from base.models import MailList


# Register your models here.
class MailListAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', ]
    list_display_links = ['email', ]
    search_fields = ['email', ]


admin.site.register(MailList, MailListAdmin)
