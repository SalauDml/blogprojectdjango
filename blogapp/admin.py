from django.contrib import admin
from .models import BlogPost,category,tag,Comments
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(category)
admin.site.register(tag)
admin.site.register(Comments)
