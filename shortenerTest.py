# -*- coding: utf-8 -*-

import unittest

from shortener import Shortener

class TestShortener(unittest.TestCase):

   def testShortenNothing(self):
     assert shortener.shorten('') == ''

   def testShortenAnUrl(self):
     assert shortener.shorten('http://www.valtech.fr/') == 'c8d2' # c8d2fca21b2386349dddb906f666a7c9b227f4c4

   def testShortenALongUrl(self):
     assert shortener.shorten('http://www.slideshare.net/jimmybourassa/introduction-google-app-engine-waq-2011-7088970') == '62f0' # 62f02e13fe2a1553ea47208fd6a30e4191ebcb76

   def testShortenAnUrlWithLimit(self):
     assert shortener.shorten('http://www.valtech.fr/', 2) == 'c8'

   def testShortenAnUrlWithALongLimit(self):
     assert shortener.shorten('http://www.valtech.fr/', 7) == 'c8d2fca'

   def testShortenALongUrlWithALimit(self):
     assert shortener.shorten('http://www.slideshare.net/jimmybourassa/introduction-google-app-engine-waq-2011-7088970', 10) == '62f02e13fe'


if __name__=="__main__":
   shortener = Shortener()
   unittest.main()

