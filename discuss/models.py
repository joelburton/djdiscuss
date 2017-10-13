from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Discussion(models.Model):
    """Discussion thread.

    A thread is like a container for comments. A thread can be attached to any piece of
    content in the site.
    """

    content_type = models.ForeignKey(
        ContentType,
    )

    object_id = models.CharField(
        max_length=255,
    )

    content = GenericForeignKey()

    class Meta:
        unique_together = ['content_type', 'object_id']

    def __str__(self):
        return "Discussion {id} on {content}".format(
            id=self.id,
            content=self.content,
        )


@python_2_unicode_compatible
class Comment(models.Model):
    """Discussion comment.

    A comment in a discussion thread.
    """

    discussion = models.ForeignKey(
        Discussion,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    text = models.TextField(
        help_text='The content of the comment.'
    )

    upload = models.FileField(
        upload_to="discuss/%Y/%m/%d/",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "Comment:{comment} from discussion:{discussion}".format(
            comment=self.id,
            discussion=self.discussion.id,
        )


@python_2_unicode_compatible
class CommentReadStatus(models.Model):
    """ Tracking if a user involved in a discussion has read the most recent
    comment in order to surface unread comments first.
    """

    comment = models.ForeignKey(
        Comment,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    read_at = models.DateTimeField(
        auto_now_add=True,
    )

    has_read = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return "Comment:{comment} has {status} read status.".format(
                                comment=self.comment.id,
                                status=self.has_read,
                                )