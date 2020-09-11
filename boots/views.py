from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect

from .models import Boot, Brand, Review
from .forms import ProductForm, commentForm
# Create your views here.


def all_boots(request):
    """ A view to show all boots, including sorting and search queries """

    boots = Boot.objects.all()
    query = None
    brands = None
    sort = None
    direction = None

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
                messages.error(request, "You didn't enter a valid search!")
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
    reviews = boot.reviews.all()
    context = {
        'boot': boot,
        'reviews': reviews,
    }

    return render(request, 'boots/boot_detail.html', context)


@login_required
def add_product(request):
    """ Add a pair of boots to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = form.save()
            messages.success(request, 'Successfully added Boots!')
            return redirect(reverse('boot_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add Boots. Please ensure the form is valid.')
    else:
        form = ProductForm()
        

    template = 'boots/add_boot.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Boot, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('boot_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'boots/edit_boot.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Boot, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('boots'))


def addreview(request, boot_id):
    """ Add the comments to the DB """
    if request.method == 'POST':
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            data = Review()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.boot = Boot.objects.get(id=boot_id)
            data.save()
            messages.success(request, 'Successfully added a review!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Failed to add comment.')
