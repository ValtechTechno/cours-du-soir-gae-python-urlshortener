import re

class UrlCleaner():

  def clean(self, urlToClean):

    if not urlToClean.startswith('http://') and not urlToClean.startswith('https://'):
      raise ValueError('Bad protocol. It should start with "http://" or "https://"')

    if urlToClean.startswith('http://localhost') or urlToClean.startswith('https://localhost'):
      raise ValueError('Cannot refer to localhost')

    if urlToClean.startswith('http://127.0.0.1') or urlToClean.startswith('https://127.0.0.1'):
      raise ValueError('Cannot refer to localhost')

    if urlToClean.startswith('http://192.168.') or urlToClean.startswith('https://192.168.'):
      raise ValueError('Cannot refer to lan address')

    if urlToClean.startswith('http://172.16.') or urlToClean.startswith('https://172.16.'):
      raise ValueError('Cannot refer to lan address')

    if urlToClean.startswith('http://valte.ch') or urlToClean.startswith('http://shorten-url.appspot.com'):
      raise ValueError('Cannot refer to self address')

    # Remove strange characters
    return re.sub('[<>\"\']', '', urlToClean) 
