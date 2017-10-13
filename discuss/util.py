"""Utilities for discussion."""

from django.contrib.contenttypes.models import ContentType

from discuss.models import Discussion, CommentReadStatus


def get_discussion(obj):
    """Get threads for an object."""

    type_ = ContentType.objects.get_for_model(obj)
    threads = Discussion.objects.filter(content_type__pk=type_.id, object_id=obj.id)
    return threads.first()


def mark_read(discussion, user):
    """Mark discussion as read."""

    if not user.is_anonymous():
        read = CommentReadStatus.objects.filter(
            comment__discussion=discussion,
            user=user,
            has_read=True)
        unread = discussion.comment_set.exclude(id__in=read)
        CommentReadStatus.objects.bulk_create(
            [CommentReadStatus(user=user, comment=c) for c in unread]
        )
