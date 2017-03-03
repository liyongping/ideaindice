#-*-coding:utf-8-*-

import os

import tornado.wsgi
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import DEBUG
from model.tables import engine
from handler.admin import *


urls = [(r"/", MainHandler)]

settings = dict(
            blog_title=u"Lee Blog",
            template_path=(os.path.join(os.path.dirname(__file__), "templates")),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="88oETzKXQAGaYdkL6gEmGeJJFYYh7EQnp3XdTP1o/Vo=",
            login_url="/admin/login",
            debug=DEBUG,
        )

class WsgiApplication(tornado.wsgi.WSGIApplication):
    def __init__(self):
        tornado.wsgi.WSGIApplication.__init__(self, urls, **settings)
        # Have one global connection to the blog DB across all handlers
        self.db = scoped_session(sessionmaker(bind=engine))

