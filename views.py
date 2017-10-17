from django.shortcuts import render

# Create your views here.

class Admin_Stat_Ip(View):

        def get(self, request, order_id):
            order = get_object_or_404(Order, id=order_id)
            return render(request, 'admin/statistique/ip.html', {'order': order})


        def post(self, request):
            pass
