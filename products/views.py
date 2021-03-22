from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Category
from profiles.models import UserProfile
from .forms import NewReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                else:
                    sortkey = f'{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details & reviews """
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    can_review = profile.orders.filter(lineitems__product_id=product_id)
    print(can_review)

    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.created_by = profile
            review.save()
            messages.success(request, 'Your review has been posted, thanks!')

    print('outer_loop')
    context = {
        'product': product,
        'can_review': can_review,
    }

    return render(request, 'products/product_detail.html', context)

