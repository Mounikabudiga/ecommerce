from django.contrib import admin

# Register your models here.
from .models import product_field,user_field,buyer

admin.site.register(product_field)

admin.site.register(user_field)

admin.site.register(buyer)
