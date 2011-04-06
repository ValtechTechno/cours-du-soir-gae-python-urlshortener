import hashlib

class Shortener():

  def shorten(self, text, limit = 4):
    if len(text) == 0:
     return text
    m = hashlib.sha1()
    m.update(text)
    r = m.hexdigest()
    return r[0:limit]
