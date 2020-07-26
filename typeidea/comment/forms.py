# -*- coding: utf-8 -*-
# @Author  : xiaohao
# @Email   : 321459055@qq.com
# @File    : forms.py
# @Software: PyCharm
# @Time    : 2020/7/23 17:45

import mistune
from ckeditor.widgets import CKEditorWidget
from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )
    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )
    website = forms.CharField(
        label='网站',
        max_length=100,
        widget=forms.URLInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )
    # content = forms.CharField(
    #     label="内容",
    #     max_length=500,
    #     widget=forms.widgets.Textarea(
    #         attrs={'rows': 6, 'cols': 60, 'class': 'form-control'}
    #     )
    # )
    content = forms.CharField(widget=CKEditorWidget(), label='内容', required=True)

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度怎么能这么短呢！！')
        content = mistune.markdown(content)
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
