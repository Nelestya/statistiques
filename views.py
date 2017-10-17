from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Ipadress
# Create your views here.

class Admin_Stat_Ip(View):

        def get(self, request, ipadress_id):
            adresseip = get_object_or_404(Ipadress, id=ipadress_id)
            context = {'adresseip': adresseip}
            return render(request, 'admin/statistique/ip.html', context)


        def post(self, request):
            pass
