import json
from django.db import models
from static import SORT_CHOICES, STYLE_CHOICES, PLAYING_CHOICES


class Rss(models.Model):
    sort = models.CharField(max_length=2, choices=SORT_CHOICES)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)
    hash_code = models.CharField(max_length=45, unique=True, db_index=True)
    episode_id = models.SmallIntegerField(max_length=4, null=True, blank=True)
    timestamp = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.title


class Douban(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    aka = models.CharField(max_length=3000, blank=True, null=True)
    original_title = models.CharField(max_length=200, blank=True, null=True)
    alt = models.URLField(blank=True, null=True)
    countries = models.CharField(max_length=100, blank=True, null=True)
    current_season = models.SmallIntegerField(blank=True, null=True)
    directors = models.CharField(max_length=40, blank=True, null=True)
    genres = models.CharField(max_length=400, blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    douban_id = models.BigIntegerField()
    average = models.FloatField(blank=True, null=True)
    episodes_count = models.SmallIntegerField(max_length=3, blank=True, null=True)
    summary = models.CharField(max_length=6000, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)

    def all_tags(self):
        tags = [self.title, self.original_title]
        tags.extend(self.aka_decode())
        return tags

    def aka_decode(self):
        return json.loads(self.aka)

    def countries_decode(self):
        return ','.join(json.loads(self.countries))

    def all_tags_dump(self):
        return ','.join(self.all_tags())

    def __unicode__(self):
        return self.title

class Tags(models.Model):
    title = models.CharField(max_length=200)
    sort = models.CharField(max_length=2, choices=SORT_CHOICES)
    style = models.CharField(max_length=2, choices=STYLE_CHOICES)
    tags = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.title

class Info(models.Model):
    sort = models.CharField(max_length=2, choices=SORT_CHOICES)
    title = models.CharField(max_length=200)
    tags = models.ForeignKey('Tags', blank=True, null=True)
    douban = models.ForeignKey('Douban', blank=True, null=True)
    weekday = models.SmallIntegerField(blank=True, null=True)
    bgm_count = models.IntegerField(blank=True, null=True)
    now_playing = models.SmallIntegerField(default=0, choices=PLAYING_CHOICES)
    #image = models.ImageField(upload_to='info_pic', blank=True, null=True)
    images = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title
