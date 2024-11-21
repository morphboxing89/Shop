from django.contrib import admin


from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

#Регистрация моделей


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'discount', 'quantity', 'category']
    list_editable = ['discount', 'quantity',]
    search_fields = ['name', 'description',]
    list_filter = ['discount', 'quantity', 'category']
