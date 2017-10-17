from django.contrib import admin
import datetime
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse
from .models import Ipadress

# Register your models here.

def stats_ip_page(obj):
    return '<a href="{}">ListPage</a>'.format(reverse('statistiques:admin_ip_detail', args=[obj.id]))
stats_ip_page.allow_tags = True

class IpadressAdmin(admin.ModelAdmin):
    list_display = ['ip', stats_ip_page]

admin.site.register(Ipadress, IpadressAdmin)
