from django.db import models


class ProductModel(models.Model):
    sku = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    category_productAmount = models.IntegerField(null=True, blank=True)
    discount_price = models.IntegerField(null=True, blank=True)
    full_price = models.IntegerField(null=True, blank=True)
    availability = models.IntegerField(null=True, blank=True)
    orders = models.IntegerField(null=True, blank=True)
    # photos = models.CharField(max_length=1000, null=True, blank=True)

    product_rating = models.FloatField(null=True, blank=True)
    # product_tags = models.CharField(max_length=50, null=True, blank=True)
    seller_id = models.IntegerField(null=True, blank=True)
    seller_title = models.CharField(max_length=70, null=True, blank=True)
    seller_link = models.CharField(max_length=70, null=True, blank=True)
    seller_description = models.TextField(null=True, blank=True)
    seller_registrationDate = models.IntegerField(null=True, blank=True)
    seller_rating = models.FloatField(null=True, blank=True)
    seller_reviews = models.IntegerField(null=True, blank=True)
    seller_orders = models.IntegerField(null=True, blank=True)
    # seller_contacts = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('id',)
