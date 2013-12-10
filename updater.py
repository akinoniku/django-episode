from datetime import datetime
import json
import urllib2
from django.utils.timezone import UTC
from models import Rss


def loop_static_source(source_list):
    for sort, source in source_list:
        get_rss(sort, source)


def get_rss(sort, source_url):
    rss_json = urllib2.urlopen(source_url).read()
    return save_rss(sort, json.loads(rss_json)['value']['items'])


def save_rss(sort, rss_json):
    counter = 0
    for rss in rss_json:
        if not Rss.objects.filter(hash_code=rss['hash']):
            new_rss = Rss(title=rss['title'], link=rss['url'],
                          hash_code=rss['hash'], sort=sort, timestamp=datetime.now(tz=UTC(8)))
            new_rss.save()
            #analysis_tags(new_rss)
            counter += 1
        else:
            break
    if counter > 0:
        # send notification to analysis tags
        pass
    return counter
