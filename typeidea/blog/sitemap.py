# -*- coding: utf-8 -*-
# @Author  : xiaohao
# @Email   : 321459055@qq.com
# @File    : sitemap.py
# @Software: PyCharm
# @Time    : 2020/7/24 22:54
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "always"
    prority = 1.0

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return reverse('post-detail', args=[obj.pk])