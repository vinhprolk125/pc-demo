from django.contrib import admin

from .models import *

admin.site.register(Customer)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['productname','order','quantity']
admin.site.register(Order)
admin.site.register(OrderItem,OrderItemAdmin)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['address','order','customer']
admin.site.register(ShippingAddress,ShippingAddressAdmin)

class CommentInLine(admin.TabularInline):
    model = Comments
class ProductAdmin(admin.ModelAdmin):
    list_display = ['namePD','typePD','id']
    list_filter = ['typePD','namePD']
    search_fields = ['name','id']
    inline = [CommentInLine]
admin.site.register(Product,ProductAdmin)