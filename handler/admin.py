#-*-coding:utf-8-*-

from handler.base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.write("hello world")
    def post(self):
        pass
