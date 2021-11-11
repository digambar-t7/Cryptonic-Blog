from django.contrib import admin
from .models import BlogPost,BlogComment

# Register your models here.
admin.site.register(BlogComment)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinjext.js')