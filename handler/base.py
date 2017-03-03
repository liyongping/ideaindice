#-*-coding:utf-8-*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    option_dict = {}
    
    @property
    def db(self):
        return self.application.db
    
    def prepare(self):
        pass

    def on_finish(self):
        self.db.close()

