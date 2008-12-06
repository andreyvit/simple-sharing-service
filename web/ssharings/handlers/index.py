# -*- coding: utf-8 -*-

import logging

from datetime import datetime, timedelta
from google.appengine.api import memcache
from google.appengine.ext import db

from ssharings.models import *
from ssharings.handlers.base import prolog, BaseHandler

class IndexHandler(BaseHandler):
  @prolog()
  def get(self):
    self.render_and_finish('hello.html')
