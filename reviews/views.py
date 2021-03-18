from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ProductReviewForm
from products.models import Product
from .models import Review



# Create your views here.
def review(request, product_id):
    return


"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    reviews = Review.objects.all(pk=product)
    form = ProductReviewForm(instance=product)
    template = 'products/product_detail.html'
    context = {
        'form': form,
        'reviews': reviews,
    }
    return render(request, template, context)

"""