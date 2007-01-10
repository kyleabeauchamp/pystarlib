"""Unit test 
"""
from STAR.Text import *
from unittest import TestCase
import unittest


class AllChecks(TestCase):
    def test(self):
        """Text"""
        textExpectedAfterCollapse = ';<eol-string>mmy xie<eol-string>;\n_Test'
        text = """;
mmy xie
;
_Test"""
        textCollapsed = semicolon_block_collapse( text )
        self.assertEqual( textExpectedAfterCollapse, textCollapsed)

        value, pos = tag_value_quoted_parse( textCollapsed, 0 )
        valueExpected = '\nmmy xie\n'
        posExpected = 34
        self.assertEqual( valueExpected, value )
        self.assertEqual( posExpected, pos)
        
        t2 = """
; my text ## is no comment
;
## comment 1
value ## comment 2
"""
        t2noComment = """
; my text ## is no comment
;
value
"""
        self.assertEqual(t2noComment,comments_strip( t2 ))

if __name__ == "__main__":
    unittest.main()
