# -*- coding: utf-8 -*-

import unittest
import sys

class TestShortUrl(unittest.TestCase):

   def setUp(self):
     self.testbed = testbed.Testbed()	# First, create an instance of the Testbed class.
     self.testbed.activate() # Then activate the testbed, which prepares the service stubs for use.
     self.testbed.init_datastore_v3_stub() # Next, declare which service stubs you want to use.

   def tearDown(self):
     self.testbed.deactivate()


if __name__=="__main__":
   sys.path.insert(0, '/home/paulgreg/Applications/google_appengine/')
   import dev_appserver
   dev_appserver.fix_sys_path()

   from google.appengine.ext import db
   from google.appengine.ext import testbed

   unittest.main()

