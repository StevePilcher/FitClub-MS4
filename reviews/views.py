from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ProductReviewForm
from products.models import Product
from profiles.models import UserProfile


def review(request):
    """ Update product reviews"""

