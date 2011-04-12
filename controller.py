import cgi
import datetime
import os
import logging

from urlModel import UrlModel
from urlModel import UrlController

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

def goToHome(self, error = None):
  lasts = urlController.get_lasts()
  self.response.headers['Content-Type'] = 'text/html'
  path = os.path.join(os.path.dirname(__file__), 'home.html')
  self.response.out.write(template.render(path, { 'lasts': lasts, 'error': error } ))

class MainPage(webapp.RequestHandler):
  def get(self): 
    goToHome(self)

class SavePage(webapp.RequestHandler):
  def post(self):
    url = self.request.get('url')
    if not url or len(url) == 0: 
      goToHome(self, 'Please type an URL.')
      return

    if not url.startswith('http://') and not url.startswith('https://'):
      goToHome(self, 'URL should start with "http://" or "https://".')
      return

    shortened_url = urlController.save(url)
    self.redirect('/')

class RedirectPage(webapp.RequestHandler):
  def get(self, shortname):
    shortened_url = urlController.get_by_key(shortname)
    self.redirect(shortened_url.url)

class RssPage(webapp.RequestHandler):
  def get(self):
    lasts = urlController.get_lasts()
    self.response.headers['Content-Type'] = 'application/rss+xml'
    path = os.path.join(os.path.dirname(__file__), 'rss.xml')
    self.response.out.write(template.render(path, { 'lasts': lasts } ))


application = webapp.WSGIApplication([
													('/', MainPage),
													('/add', SavePage),
													('/rss.xml', RssPage),
													(r'/(.*)', RedirectPage)
												])

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.DEBUG)
  urlController = UrlController()
  run_wsgi_app(application)
