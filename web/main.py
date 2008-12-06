#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from ssharings.handlers.index import IndexHandler

url_mapping = [
  ('/', IndexHandler),
]

def main():
  application = webapp.WSGIApplication(url_mapping, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
