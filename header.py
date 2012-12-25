#!/usr/bin/env python
#! coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
#公共头部信息
class Header(tornado.web.UIModule):
    def render(self,entry,show_comments=False):
        return self.render_string(
            "header.html",entry=entry,show_comments=show_comments
        )