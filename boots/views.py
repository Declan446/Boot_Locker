from django.shortcuts import render, get_object_or_404
from .models import Boot

# Create your views here.


def all_boots(request):
    """ A view to show all boots, including sorting and search queries """

    boots = Boot.objects.all()

    context = {
        'boots': boots,
    }

    return render(request, 'boots/boots.html', context)


def boot_detail(request, boot_id):
    """ A view to show selected boot detail """

    boot = get_object_or_404(Boot, pk=boot_id)

    context = {
        'boot': boot,
    }

    return render(request, 'boots/boot_detail.html', context)
