from django.conf.urls import url
from .views import Order_Create, Admin_Order_Detail, Admin_Order_Pdf
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'orders'
urlpatterns = [
    url(r'^admin/order/(?P<ip>\d+)/$', staff_member_required(Admin_Stat_Ip.as_view()), name='admin_ip_detail'),
]
