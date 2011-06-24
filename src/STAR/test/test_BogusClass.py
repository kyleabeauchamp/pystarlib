# Already the first line should throw a ImportWarning.
from nose.plugins.skip import SkipTest
from unittest import TestCase
import unittest

try:
    from STAR.bogusClass import bogusParameter #@UnusedImport
except:
    raise SkipTest

class AllChecks(TestCase):
    
    # New to python 2.7
    #@unittest.skipIf(self.ignoreThisSuite, 'not supported in this library version') #@UndefinedVariable
    def test_BogusClass(self):
        self.assertEqual( bogusParameter = 1 )
   
if __name__ == "__main__":
    unittest.main()
