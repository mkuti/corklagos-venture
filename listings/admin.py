from django.contrib import admin
from .models import Listing, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Listing)
admin.site.register(Category, CategoryAdmin)
