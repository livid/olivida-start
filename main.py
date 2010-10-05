#!/usr/bin/env python

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'tpl', 'index.html')
    output = template.render(path, template_values)
    self.response.out.write(output)

def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()