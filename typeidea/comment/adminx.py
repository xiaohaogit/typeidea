# Register your models here.
import xadmin
from comment.forms import CommentForm
from comment.models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    form = CommentForm
    list_display = ["target", "nickname", "content", "website", "created_time"]



