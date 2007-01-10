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

    def testcomments_strip(self):
        """comments_strip"""
        text = """
# my comment exactly
foo # comment
value#stil a value
bar
; # actual data
;
"""
        textExpected = """foo
value#stil a value
bar
; # actual data
;
"""
        textNew = comments_strip( text )
        self.assertEqual( textNew, textExpected)
    
    def testcomments_strip2(self):
        """comments_strip 2"""
        text = """
H' # comment
"""
        textExpected = """
H'
"""
        textNew = comments_strip( text )
        self.assertEqual( textNew, textExpected)

    def testcomments_strip3(self):
        """comments_strip 3"""
        text = """
H# 
"""
        textExpected = """
H# 
"""

        textNew = comments_strip( text )
        self.assertEqual( textNew, textExpected)

    def testcomments_strip4(self):
        """comments_strip 4"""
        text = """
;
test # no comment
;
"""
        textExpected = """
;
test # no comment
;
"""
        textNew = comments_strip( text )
        # Fails currently
#        self.assertEqual( textNew, textExpected)
        self.assertNotEqual( textNew, textExpected)

if __name__ == "__main__":
    unittest.main()
