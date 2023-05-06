from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)                                                                           # Register page with decorator
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}                                                       # Auto changing slug by name

@admin.register(Product)                                                                            # Register page with decorator
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}                                                      # Auto changing slug by title