from django.contrib import admin

# Register your models here.

from .models import products,Category,OrderModel,comment

admin.site.register(products)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(comment)
