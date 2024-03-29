"""
Unit test execute as:
python $PYSTARLIB_ROOT/src/STAR/test/test_Utils.py
"""
from STAR.Utils import Lister
from STAR.Utils import transpose
from unittest import TestCase
import unittest


class AllChecks(TestCase, Lister):
    """Test case"""
    def test_afew(self):
        """STAR Utils"""
        m1 = [ [1, 2], [3, 4] ]
        m2 = [ (1, 3), (2, 4) ]        
        m1t= transpose(m1)
        self.assertTrue(m1t==m2)

if __name__ == "__main__":
    unittest.main()
