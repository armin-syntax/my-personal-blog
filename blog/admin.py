from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Tag, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    exclude = ['slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'is_published', 'created_at', 'updated_at']
    list_filter = ['is_published', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'content']
    exclude = ['slug']
    actions = ['publish', 'unpublish']

    def get_actions(self, request):
        actions = super().get_actions(request)

        if not Post.objects.filter(is_published=False).exists():
            if 'publish' in actions:
                del actions['publish']
        
        if not Post.objects.filter(is_published=True):
            if 'unpublish' in actions:
                del actions['unpublish']
        
        return actions

    def publish(self, request, queryset):
        queryset = queryset.filter(is_published=False)
        updated = queryset.update(is_published=True)

        if updated > 0:
            self.message_user(
                request,
                ngettext(
                    f"Successfully published {updated} post.",
                    f"Successfully published {updated} posts.",
                    updated
                ),
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "No posts were affected by this action",
                messages.WARNING,
            )
    publish.short_description = 'Publish selected posts'

    def unpublish(self, request, queryset):
        queryset = queryset.filter(is_published=True)
        updated = queryset.update(is_published=False)

        if updated > 0:
            self.message_user(
                request,
                ngettext(
                    f"Successfully unpublished {updated} post.",
                    f"Successfully unpublished {updated} posts.",
                    updated
                ),
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "No posts were affected by this action",
                messages.WARNING,
            )
    unpublish.short_description = 'Unpublish selected posts'
