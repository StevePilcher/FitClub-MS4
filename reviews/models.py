from django.db import models

from products.models import Product
from profiles.models import UserProfile


# Create your models here.
class Review(models.Model):
    sku = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    review_title = models.CharField(max_length=50, null=True, blank=False)
    review_user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    review_desc = models.CharField(max_length=500, blank=False)
    review_date = models.DateField()
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)

    def __str__(self):
        return self.review_title
