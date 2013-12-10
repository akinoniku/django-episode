# coding=utf-8

RSS_SOURCES = (
    ('AN', 'http://pipes.yahoo.com/pipes/pipe.run?_id=2a1aee3dda9a657eaa4d8eece5441f8f&_render=json'),
    ('EP', 'http://pipes.yahoo.com/pipes/pipe.run?_id=4059b898dc1eef8661b3eabcfc1d905a&_render=json'),
)

STYLE_CHOICES = (
    ('TM', '字幕组'),
    ('TL', '作品名'),
    ('CL', '清晰度'),
    ('FM', '格式'),
    ('LG', '字幕语言'),
)

SORT_CHOICES = (
    ('AN', '动画'),
    ('EP', '剧集'),
)

PLAYING_CHOICES = (
    (0, '已完结'),
    (1, '连载中'),
    (2, '长篇'),
    (3, '废弃'),
)
