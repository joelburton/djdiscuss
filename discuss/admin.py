from django.contrib import admin

from discuss.models import Discussion, Comment, CommentReadStatus


class CommentInline(admin.TabularInline):
    """Inline of comment on thread."""

    model = Comment
    fields = ['author', 'text', 'created_at']
    extra = 0
    readonly_fields = ['created_at']
    show_change_link = True


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    """Admin for discussion threads."""

    inlines = [CommentInline]


class CommentReadStatusInline(admin.TabularInline):
    """Inline of read status for a comment."""

    model = CommentReadStatus
    fields = ['user', 'read_at', 'has_read']
    extra = 0
    readonly_fields = ['user', 'read_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin for comments."""

    readonly_fields = ['discussion', 'created_at']
    inlines = [CommentReadStatusInline]

    def has_add_permission(self, request):
        """Don't allow adding via admin."""

        return False
