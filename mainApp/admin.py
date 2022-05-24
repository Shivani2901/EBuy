from django.contrib import admin
from .models import *

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Category)
# admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(Contact)
admin.site.register(Profile)


