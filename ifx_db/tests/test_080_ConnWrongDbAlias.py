# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_080_ConnWrongDbAlias(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_080)

  def run_test_080(self):
    try:
      conn = ifx_db.connect("x", config.user, config.password)
      print "??? No way."
    except:
      print ifx_db.conn_error()
 
    #if conn:
    #  print "??? No way."
    #else:
    #  print ifx_db.conn_error()

#__END__
#__LUW_EXPECTED__
#08001
#__ZOS_EXPECTED__
#08001
#__SYSTEMI_EXPECTED__
#08001
#__IDS_EXPECTED__
#08001