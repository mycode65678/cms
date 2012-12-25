#!/usr/bin/env python
#! coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web

class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

settings = {
    'debug':True,
    'template_path':'view',
}
app = tornado.web.Application([
    (r"/",Index),
    (r"/js/(.*)",tornado.web.StaticFileHandler,{'path':"js"}),
    (r"/css/(.*)",tornado.web.StaticFileHandler,{'path':"css"}),
    (r"/img/(.*)",tornado.web.StaticFileHandler,{'path':"img"}),
    ],**settings)

if __name__ == "__main__":
    h = tornado.httpserver.HTTPServer(app)
    h.listen(81)
    tornado.ioloop.IOLoop.instance().start()