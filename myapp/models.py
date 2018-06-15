# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Poem(models.Model):
    poet = models.CharField(max_length=32, default="Null")
    text = models.TextField(null=True)

    def __str__(self):
        return self.text


# class Blog(models.Model):
#     Name = models.CharField(max_length=100, blank=True)
#     Content = UEditorField(u'内容	', width=600, height=300, toolbars="full", imagePath="", filePath="",
#                            upload_settings={"imageMaxSize": 1204000}, settings={}, command=None,
#                            event_handler=None, blank=True)


class Article(models.Model):
    title = models.CharField(u"博客标题", max_length=100)  # 博客标题
    category = models.CharField(u"博客标签", max_length=50)  # 博客标签
    status = models.CharField(u"文章状态（默认1：所有人可见；0：登陆账户可见）",max_length=10);
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)  # 博客发布日期
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    content = UEditorField(u"文章正文", height=300, default=u'', blank=True, imagePath="./uploads/blog/images/",
                           toolbars='full', filePath='./uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
