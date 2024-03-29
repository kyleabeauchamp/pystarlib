"""
Unit test for SaveFrameTest.py
Setup taken from "Dive Into Python"
"""
from STAR.TagTable import TagTable
import unittest
from unittest import TestCase
from STAR.SaveFrame import SaveFrame


class AllChecks(TestCase):
    """Test case"""
    sf = SaveFrame()
    tT = TagTable()
    tT.tagnames=['_File_characteristics.Sf_category']
    tT.tagvalues=[['file_characteristics']]
    sf.tagtables.append(tT)
    def testcheck_integrity(self):
        """SaveFrame integritiy"""
        self.assertFalse(self.sf.check_integrity())
    def teststar_text(self):
        """SaveFrame STAR representation"""
        starText = """\nsave_general_sf_title\n   loop_\n      _File_characteristics.Sf_category\n\nfile_characteristics\n\n   stop_\n\nsave_\n""" # pylint: disable=C0301
        self.assertEqual(self.sf.star_text(), starText)
        
    def testgetSaveFrameCategory(self):
        """SaveFrame category"""
        sfCategory = "file_characteristics"
        self.assertEqual(self.sf.getSaveFrameCategory(), sfCategory)


if __name__ == "__main__":
    unittest.main()
