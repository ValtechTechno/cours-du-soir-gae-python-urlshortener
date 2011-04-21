# -*- coding: utf-8 -*-

import unittest

from urlCleaner import UrlCleaner

class TestUrlCleaner(unittest.TestCase):

   def testCleanASimpleUrl(self):
     assert urlCleaner.clean('http://www.wikipedia.org/') == 'http://www.wikipedia.org/'

   def testCleanASimpleHttpsUrl(self):
     assert urlCleaner.clean('https://wikipedia.org/') == 'https://wikipedia.org/'

   def testCleanALongVerboseUrl(self):
     assert urlCleaner.clean('http://www.google.fr/search?sourceid=chrome&client=ubuntu&channel=cs&ie=UTF-8&q=url+injecton#sclient=psy&hl=fr&client=ubuntu&hs=dKK&channel=cs&source=hp&q=app+engine+sanitize&aq=f&aqi=&aql=&oq=&pbx=1&fp=ad548885dc40634') == 'http://www.google.fr/search?sourceid=chrome&client=ubuntu&channel=cs&ie=UTF-8&q=url+injecton#sclient=psy&hl=fr&client=ubuntu&hs=dKK&channel=cs&source=hp&q=app+engine+sanitize&aq=f&aqi=&aql=&oq=&pbx=1&fp=ad548885dc40634'

   def testCleanAStrangeUrl(self):
     assert urlCleaner.clean('http://www.cwi.nl:80/%7Eguido/Python.html') == 'http://www.cwi.nl:80/%7Eguido/Python.html'

   def testCleanABadUrl(self):
     assert urlCleaner.clean('http://"\'<>test') == 'http://test'

   def testThrowAnErrorIfNotAnHttpUrl(self):
     try:
       urlCleaner.clean('ftp://someserver')
       assert False
     except ValueError, e:
        assert True
        assert e.args[0] == 'Bad protocol. It should start with "http://" or "https://"'

   def testThrowAnErrorIfUrlIsLocalhost(self):
     try:
       urlCleaner.clean('http://localhost/some/path')
       assert False
     except ValueError, e:
        assert True
        assert e.args[0] == 'Cannot refer to localhost'

   def testThrowAnErrorIfUrlIsLocalhostOnOtherPort(self):
     try:
       urlCleaner.clean('http://localhost:8080/some/path')
       assert False
     except ValueError, e:
        assert True
        assert e.args[0] == 'Cannot refer to localhost'

   def testThrowAnErrorIfUrlIsLocalhostIpV4(self):
     try:
       urlCleaner.clean('http://127.0.0.1/some/path')
       assert False
     except ValueError, e:
        assert True
        assert e.args[0] == 'Cannot refer to localhost'

   def testThrowAnErrorIfUrlIsOnLanClassC(self):
     try:
       urlCleaner.clean('http://192.168.0.1/some/path')
       assert False
     except ValueError, e:
        assert True
        assert e.args[0] == 'Cannot refer to lan address'

   def testThrowAnErrorIfUrlIsOnLanClassB(self):
     try:
       urlCleaner.clean('http://172.16.32.1/some/path')
       assert False
     except ValueError, e:
        assert True
        assert e.args[0] == 'Cannot refer to lan address'


if __name__=="__main__":
   urlCleaner = UrlCleaner()
   unittest.main()

