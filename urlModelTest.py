# -*- coding: utf-8 -*-

import unittest
import sys

class TestShortUrl(unittest.TestCase):

   def setUp(self):
     self.testbed = testbed.Testbed()	# First, create an instance of the Testbed class.
     self.testbed.activate() # Then activate the testbed, which prepares the service stubs for use.
     self.testbed.init_datastore_v3_stub() # Next, declare which service stubs you want to use.


   def testInsertEntity(self):
     UrlModel().put()
     self.assertEqual(1, len(UrlModel.all().fetch(10)))

   def testFind_shortname(self):
      self.assertEqual('fa', urlController.find_shortname('http://valtech.com/'))
      urlController.save('http://valtech.com/')
      self.assertEqual('fa4', urlController.find_shortname('http://valtech.com/'))

   def testSave(self):
     o = urlController.save('http://valtech.com/some_long_url')
     assert o != None
     self.assertEqual(o.url, 'http://valtech.com/some_long_url')
     self.assertEqual(o.shortname, '95')
     self.assertEqual(1, len(UrlModel.all().fetch(10)))

   def testSaveEmptyUrl(self):
     o = urlController.save('')
     self.assertEqual(0, len(UrlModel.all().fetch(10)))

   def testSaveSameUrl(self):
     urlController.save('http://valtech.com/some_long_url')
     self.assertEqual(1, len(UrlModel.all().fetch(10)))
     urlController.save('http://valtech.com/some_long_url')
     self.assertEqual(1, len(UrlModel.all().fetch(10)))

   def testGetByUrlWhenNotHere(self):
     o = urlController.get_by_url('http://valtech.com/');
     assert not o

   def testGetByUrl(self):
     urlController.save('http://valtech.com/')
     o = urlController.get_by_url('http://valtech.com/');
     assert o != None
     self.assertEqual('fa', o.shortname)

   def testGetByKey(self):
     urlController.save('http://valtech.com/')
     o = urlController.get_by_key('fa');
     assert o != None
     self.assertEqual('http://valtech.com/', o.url)
     self.assertEqual(1, o.hits)
     o = urlController.get_by_key('fa');
     self.assertEqual(2, o.hits)

   def testGetLasts(self):
     l = urlController.get_lasts()
     assert l == None

     urlController.save('http://valtech.com/')
     urlController.save('http://google.com/')
     l = urlController.get_lasts()

     self.assertEqual(2, len(l))
     self.assertEqual('http://valtech.com/', l[1].url)
     self.assertEqual('http://google.com/', l[0].url)


   def tearDown(self):
     self.testbed.deactivate()


if __name__=="__main__":
   sys.path.insert(0, '/home/paulgreg/Applications/google_appengine/')
   import dev_appserver
   dev_appserver.fix_sys_path()

   from urlModel import UrlModel
   from urlModel import UrlController

   from google.appengine.ext import db
   from google.appengine.ext import testbed

   urlController = UrlController()
   unittest.main()

