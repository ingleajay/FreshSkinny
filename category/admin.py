from django.contrib import admin
from .models import Category

# populate slug with category name
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('category_name',)
    }
    list_display=('category_name','slug')
admin.site.register(Category,CategoryAdmin)