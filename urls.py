from django.conf.urls import url
from .views import Admin_Stat_Ip
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'statistiques'
urlpatterns = [
    url(r'^admin/statistique/(?P<ipadress_id>\d+)/$', staff_member_required(Admin_Stat_Ip.as_view()), name='admin_ip_detail'),
]
