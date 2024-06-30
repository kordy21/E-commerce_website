from django.contrib import admin

# Register your models here.
from .models import Category,Product,Cart,Cartitems

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register( Product,ProductAdmin )
admin.site.register(Cart)
admin.site.register(Cartitems)