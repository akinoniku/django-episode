# coding=utf-8
from datetime import datetime
import json
import urllib2
from django.utils.timezone import UTC
from models import Rss, Info
import re

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

def clean_info_title(title):
    """ 删除‘第二季’之类的字符和括号及括号以内的字符

    Args:
        title: a string
    Returns:
        A cleaned string
    TODO: for Ricter
    """
    m = re.match(ur'(.*)[\s\S]+第[\w\W]季', title.split('（')[0].decode('utf-8'))
    if m: return m.group(1).encode('utf-8')
    return title.split('（')[0]

def update_info_list(sort, info_list):
    """ 保存 info_list 里面的新番信息到 Info Model

    当新的info_list传入，监测json更变，如果之前now_playing 为连载中的消失了，把now_playing设成 完结
    如果是不在Info中的，添加它

    Args:
        sort: SORT_CHOICES
        info_list: a object of info list, not a json
    Returns:
        An int counter counting changed info obj
    TODO: for Ricter
    """
    serial_list = [str(data) for data in Info.objects.all()]
    info_title_list = [clean_info_title(info['title'].encode('utf-8')) for info in info_list]
    for info in info_list:
        clean_title = clean_info_title(info['title'].encode('utf-8'))
        if not clean_title in serial_list:
            Info(
                sort = sort,
                title = clean_title,
                tags = None,
                douban = None,
                weekday = info['weekday'],
                bgm_count = info['bgmcount'],
                images = info['cover'],
                now_playing = 0
            ).save()
    for serial in serial_list:
        if not serial in info_title_list:
            p = Info.objects.get(title=serial)
            p.now_playing = 1
            p.save()

    """for data in Info.objects.all():
        print data
    print Info.objects.all().count(), len(info_list)"""
    return abs(len(serial_list) - len(info_list))
