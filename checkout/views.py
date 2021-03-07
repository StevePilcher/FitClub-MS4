from django.shortcuts import render, reverse, redirect

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ISLJHGMhoNDWXqEOPqFlNiQVFvRliWGIX7tBXkx8MYuptNpRIg3iP3F4JmTEO7x6rA3S3dSfEZL0QkPeiAfpfnY00IHUiFhXF',
        'client_secret': 'test secret key',
    }

    return render(request, template, context)
