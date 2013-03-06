# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012-2013 Bastian Kleineidam
from unittest import TestCase
from dosagelib import scraper, util


class TestComicNames(TestCase):

    def test_names(self):
        for scraperclass in scraper.get_scraperclasses():
            name = scraperclass.getName()
            self.assertTrue(name.count('/') <= 1, name)
            if '/' in name:
                comicname = name.split('/')[1]
            else:
                comicname = name
            self.assertEqual(util.asciify(comicname), comicname)
