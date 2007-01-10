"""Unit test
"""
import unittest,os
from File import *
from TagTable import *
from SaveFrame import *
from unittest import TestCase


class AllChecks(TestCase):
        strf           = File(verbosity=2)        
        
        def testparse(self):
            """STAR parse"""
            text = """data_no_comments_here

save_comment
   _Saveframe_category  comment
   loop_
        _comment
        _every_flag
        _category

;
#######################
#  BOGUS              #
#######################

;
        N
    BOGUS_CATEGORY

     stop_
save_
"""
            self.assertFalse(self.strf.parse(text=text))                                    
            self.strf.filename = self.strf.filename + 'new.str'
            self.assertFalse(self.strf.write())

        def testread2(self):
            """STAR File read"""
            # Freely available on the web so not included in package.
            entry = '1edp' # 57 kb
#            entry = '1q56' # 10 Mb takes 95 s to parse on 2GHz PIV CPU
            urlLocation = "http://www.bmrb.wisc.edu/WebModule/MRGridServlet?block_text_type=3-converted-DOCR&file_detail=3-converted-DOCR&pdb_id=%s&program=STAR&request_type=archive&subtype=full&type=entry" % (entry)
            fnamezip = entry+".zip"
#            print "DEBUG: downloading url:", urlLocation
            urllib.urlretrieve(urlLocation,fnamezip)
#            print "DEBUG: opening local zip file:", fnamezip
            zfobj = zipfile.ZipFile(fnamezip)
            fname = None
            for name in zfobj.namelist():    
                if name.endswith('.str'):
                    fname = name
            self.assertTrue(fname)
                
            fnameLocal = entry+".str"
#            print "DEBUG: materializing file", fname, "as local STAR file:", fnameLocal
            outfile = open(fnameLocal, 'w')
            outfile.write(zfobj.read(fname))
            outfile.close()
            strf = File()                
            strf.filename  = fnameLocal   
#            print "DEBUG: parsing file"
            strf.read()   

if __name__ == "__main__":
    unittest.main()
