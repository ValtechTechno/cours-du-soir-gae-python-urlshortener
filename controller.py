import cgi
import datetime
import os
import logging

from urlModel import UrlModel
from urlModel import UrlController

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self): 
    self.goToHome()

  def goToHome(self):
    lasts = urlController.get_lasts()
    self.response.headers['Content-Type'] = 'text/html'
    path = os.path.join(os.path.dirname(__file__), 'home.html')
    self.response.out.write(template.render(path, { 'lasts': lasts } ))

class SavePage(webapp.RequestHandler):
  def post(self):
    shortened_url = urlController.save(self.request.get('url'))
    self.redirect('/')

class RedirectPage(webapp.RequestHandler):
  def get(self, shortname):
    shortened_url = urlController.get_by_key(shortname)
    self.redirect(shortened_url.url)

application = webapp.WSGIApplication([
													('/', MainPage),
													('/add', SavePage),
													(r'/(.*)', RedirectPage)
												])

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.DEBUG)
  urlController = UrlController()
  run_wsgi_app(application)
