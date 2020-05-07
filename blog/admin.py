from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'owner', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'owner')
    search_fields = ('title', 'skeleton')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

