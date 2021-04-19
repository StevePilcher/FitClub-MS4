from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Category, Review
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
    """ A view to show individual
    product details & enable review
     if the user has purchased the
     product before and/or left a review already"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product_id=product.id)
    template = 'products/product_detail.html'

    if request.method == 'GET':
        if request.user.is_active:
            profile = get_object_or_404(UserProfile, user=request.user)
            owns_item = profile.orders.filter(lineitems__product_id=product_id)
            if owns_item:
                for review in reviews:
                    if review.created_by == profile:
                        context = {
                            'product': product,
                            'reviews': reviews,
                            'can_review': False,
                        }
                        print("has item but already reviewed")
                        return render(request, template, context)
                else:
                    context = {
                        'product': product,
                        'reviews': reviews,
                        'can_review': True,
                    }
                    print("Owns but hasn't reviewed yet")
                    print(context)
                    return render(request, template, context)

            if reviews:
                context = {
                    'product': product,
                    'reviews': reviews,
                    'can_review': True,
                }
                print("has item but no review posted")
                return render(request, template, context)

    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.created_by = profile
            review.save()
            messages.success(request, "You've left a review, thanks!")

    reviews = Review.objects.filter(product_id=product.id)
    context = {
        'product': product,
        'reviews': reviews,
    }
    print("anonymous user, or user does not own/has reviewed the product")
    return render(request, template, context)
