from django.contrib import admin
from eproject.models import Product,Checkout

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=["name"]

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product,ProductAdmin)
admin.site.register(Checkout)

