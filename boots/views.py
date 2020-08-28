from django.shortcuts import render
from .models import Boot

# Create your views here.


def all_boots(request):
    """ A view to show all boots, including sorting and search queries """

    boots = Boot.objects.all()

    context = {
        'boots': boots,
    }

    return render(request, 'boots/boots.html', context)
