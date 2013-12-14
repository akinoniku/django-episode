from django.db import models
from static import SORT_CHOICES


class Rss(models.Model):
    sort = models.CharField(max_length=2, choices=SORT_CHOICES)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)
    hash_code = models.CharField(max_length=45, unique=True, db_index=True)
    episode_id = models.SmallIntegerField(max_length=4, null=True, blank=True)
    timestamp = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.title