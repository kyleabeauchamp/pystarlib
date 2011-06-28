# Already the first line should throw a ImportWarning.
from STAR.Utils import MySkipTest
from unittest import TestCase
import unittest

try:
    from STAR.bogusClass import bogusParameter #@UnusedImport
except:
    raise MySkipTest

class AllChecks(TestCase):
    """Test case"""    
    # New to python 2.7
    #@unittest.skipIf(self.ignoreThisSuite, 'not supported in this library version') #@UndefinedVariable
    def test_BogusClass(self):
        self.assertEqual( bogusParameter = 1 )
   
if __name__ == "__main__":
    unittest.main()
