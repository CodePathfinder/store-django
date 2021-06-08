from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
	list_display = ('cart_id', 'date_added')
	
	
class CartItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'product', 'cart', 'user', 'quantity', 'is_active')
	list_display_links = ('id', 'product')
	

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
