from django.contrib import admin
import datetime
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse

# Register your models here.

def stats_ip_page(obj):
    return '<a href="{}">ListPage</a>'.format(reverse('statistique:admin_ip_detail', args=[obj.id]))
order_detail.allow_tags = True

class OrderAdmin(admin.ModelAdmin):
    list_display = ['ip', stats_ip_page]
    
