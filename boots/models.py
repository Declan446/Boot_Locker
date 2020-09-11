from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Boot(models.Model):
    """ Model for the boots(products) """
    category = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    style = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    colour = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    boot = models.ForeignKey('Boot', null=True, blank=True, on_delete=models.SET_NULL, related_name='reviews')
    name = models.CharField(max_length=254)
    comment = models.CharField(max_length=254)

    def __str__(self):
        return self.comment
