# -*- coding: utf-8 -*-
# @Author  : xiaohao
# @Email   : 321459055@qq.com
# @File    : base_admin.py
# @Software: PyCharm
# @Time    : 2020/7/21 16:59
from django.contrib import admin


class BaseOwnerAdmin(object):
    exclude = ['owner']

    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        return qs.filter(owner=request.user)

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_models()
