from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    submitter = models.ForeignKey(User)
    title = models.TextField(blank=True)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    created = models.DateTimeField(db_index=True, default=datetime.utcnow)
    upvotes = models.PositiveIntegerField(default=1)
    in_reply_to = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.title

    @classmethod
    def scored(cls):
        """Return a queryset with calculated scores."""
        score = 'LOG10(upvotes) + ((TIMESTAMP(created) - %d) / 45000)'
        score = score % settings.NEWS_EPOCH
        return cls.objects.extra(select={'score': score})
