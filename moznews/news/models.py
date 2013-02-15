from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    submitter = models.ForeignKey(User)
    title = models.TextField(blank=True)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    created = models.DateTimeField(db_index=True, default=datetime.utcnow)
    upvotes = models.PositiveIntegerField(default=0)
    in_reply_to = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.title
