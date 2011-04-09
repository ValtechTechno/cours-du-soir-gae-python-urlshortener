from google.appengine.ext import db

from shortener import Shortener

class UrlModel(db.Model):
  url = db.StringProperty(multiline=False)
  shortname = db.StringProperty(multiline=False)
  creation_date = db.DateTimeProperty(auto_now_add=True)

class UrlController():

  def find_shortname(self, url):
    shortener = Shortener()
    nb = 2
    while nb < 10:
      shortname = shortener.shorten(url, nb)
      o = self.get_by_key(shortname)
      if not o: return shortname
      nb = nb + 1

  def save(self, url):
    if len(url) == 0: return
    o = self.get_by_url(url)
    if not o:
      o = UrlModel()
      o.url = url
      o.shortname = self.find_shortname(url)
      o.put()
    return o

  def get_by_url(self, url):
    l = db.GqlQuery('SELECT * FROM UrlModel WHERE url = :1', url).fetch(1)
    if len(l) == 1: return l[0]
    return None

  def get_by_key(self, shortname):
    l = db.GqlQuery('SELECT * FROM UrlModel WHERE shortname = :1', shortname).fetch(1)
    if len(l) == 1: return l[0]
    return None

  def get_lasts(self, number = 25):
    l = db.GqlQuery('SELECT * FROM UrlModel ORDER BY creation_date DESC').fetch(number)
    if len(l) > 0: return l
    return None



