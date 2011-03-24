from django.db import models
from django.contrib.comments.models import Comment
from django.contrib.comments.managers import CommentManager
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel

__all__ = ('MAX_PATH_LENGTH', 'ThreadedComment')

MAX_PATH_LENGTH = 255

class ThreadedComment(MPTTModel, Comment):
    title = models.TextField(_('Title'), blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, default=None,
        related_name='children', verbose_name=_('Parent'))
    
    objects = CommentManager()

    class Meta(object):
        db_table = 'threadedcomments_comment'
        verbose_name = _('Threaded comment')
        verbose_name_plural = _('Threaded comments')
