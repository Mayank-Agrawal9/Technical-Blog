from django.contrib import admin
from .models import Category, Post,Contact

# Register your models here.

#For Configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description' , 'url', 'add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display =('title','Category',)  
    search_fields = ('title',)
    list_filter = ('Category',)
    list_per_page = 50


    class Media:
        js = ('js/script.js',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)