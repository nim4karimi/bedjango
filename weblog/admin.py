from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Import Model to admin
from .models import Post


class PostAdminModel(SummernoteModelAdmin):
    list_display = ['title']
    list_editable = ['mod_date']
    list_filter = ['pub_date']

    summernote_fields = ('body')
    class Meta:
        model = Post

admin.site.register(Post, SummernoteModelAdmin)
