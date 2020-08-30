from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Boot, Brand

# Create your views here.


def all_boots(request):
    """ A view to show all boots, including sorting and search queries """

    boots = Boot.objects.all()
    query = None
    brands = None
    sort = None
    direction = None
    style = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                boots = boots.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            boots = boots.order_by(sortkey)

        if 'style' in request.GET:
            boots = request.GET['style'].split(',')
            boots = Boot.objects.filter(style__in=boots)

        if 'category' in request.GET:
            brands = request.GET['category'].split(',')
            boots = boots.filter(category__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a valid search item!")
                return redirect(reverse('boots'))

            queries = Q(name__icontains=query) | Q(colour__icontains=query)
            boots = boots.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'boots': boots,
        'search_term': query,
        'current_brands': brands,
        'current_sorting': current_sorting,
    }

    return render(request, 'boots/boots.html', context)


def boot_detail(request, boot_id):
    """ A view to show selected boot detail """

    boot = get_object_or_404(Boot, pk=boot_id)

    context = {
        'boot': boot,
    }

    return render(request, 'boots/boot_detail.html', context)
