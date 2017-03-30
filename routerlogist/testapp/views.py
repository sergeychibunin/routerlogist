from django.shortcuts import render, get_object_or_404
from .models import Mac


def index(request):
    mac_list = Mac.objects.all()
    context = {
        'mac_list': mac_list,
    }
    return render(request, 'testapp/index.html', context)


def detail(request, mac_id):
    mac = get_object_or_404(Mac, id=mac_id)
    return render(request, 'testapp/detail.html', {'mac': mac})
