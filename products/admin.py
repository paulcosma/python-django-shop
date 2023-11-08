from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    # columns visible in the admin table
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','description','discount')


# Register your models here.
admin.site.register(Product, ProductAdmin)
# django will use ProductAdmin class on deciding how to present the list of products
admin.site.register(Offer, OfferAdmin)