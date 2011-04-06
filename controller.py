import cgi
import datetime
import os
import logging

from shortUrl import ShortUrl

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self): 
    goToHome(self)

class SavePage(webapp.RequestHandler):
  def post(self):
    shortened_url = shortUrl.save(self.request.get('url'))
    goToHome(self, shortened_url)

class RedirectPage(webapp.RequestHandler):
  def get(self, shortname):
    shortened_url = shortUrl.get_by_key(shortname)
    self.redirect(shortened_url.url)

def goToHome(self, short_url_just_added = None):
  lasts = shortUrl.get_lasts()
  self.response.headers['Content-Type'] = 'text/html'
  path = os.path.join(os.path.dirname(__file__), 'home.html')
  self.response.out.write(template.render(path, {'short_url_just_added': short_url_just_added, 'lasts': lasts } ))


application = webapp.WSGIApplication([
													('/', MainPage),
													('/add', SavePage),
													(r'/browse/(.*)', RedirectPage)
												])

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.DEBUG)
  shortUrl = ShortUrl()
  run_wsgi_app(application)
