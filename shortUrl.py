from google.appengine.ext import db

from shortener import Shortener


class ShortUrl(db.Model):
  url = db.StringProperty(multiline=False)
  shortname = db.StringProperty(multiline=False)
  creation_date = db.DateTimeProperty(auto_now_add=True)

  def save(self, url):
    shortener = Shortener()

    shortUrl = self.get_by_url(url)
    if not shortUrl:
      shortUrl = ShortUrl()
      shortUrl.url = url
      shortUrl.shortname = shortener.shorten(url)
      shortUrl.put()

  def get_by_url(self, url):
    db.GqlQuery('SELECT * FROM ShortUrl WHERE url = :1', url).fetch(1)

  def get_by_key(self, shortname):
    db.GqlQuery('SELECT * FROM ShortUrl WHERE shortname = :1', shortname).fetch(1)

  def get_lasts(self):
    db.GqlQuery('SELECT * FROM ShortUrl ORDER BY creation_date DESC').fetch(10)

