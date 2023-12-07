from django.contrib import admin
from .models import (
    Label,
    Category,
    Product,
    OrderProduct,
    Cart
)

# Register your models here.
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Cart)
