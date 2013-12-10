# coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Rss


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ModelTest(TestCase):
    def setUp(self):
        self.r = Rss.objects.create(
            sort='AN',
            title='[萌月字幕组][Little Busters! Refrain][10][简繁][1280x720 AAC]',
            link='magnet:?xt=urn:btih:eff8325811f06fa232c4d91b88f0fa937ad3d7a6',
            hash_code="eff8325811f06fa232c4d91b88f0fa937ad3d7a6",
            timestamp="2013-09-09 11:11+08:00"
        )

    def test_model_save(self):
        self.assertEqual(self.r.sort, 'AN')
        self.assertIsNotNone(self.r.timestamp, 'should not be none')