"""Unit test
"""
from localConstants import *
import unittest,os
from File import *
from TagTable import *
from SaveFrame import *
from unittest import TestCase


class AllChecks(TestCase):
        strf           = File(verbosity=2)        
        
        def testreadNWrite(self):
            """STAR File read check"""
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
            self.strf.filename = self.strf.filename + '_new.str'
            self.assertFalse(self.strf.write())

        def testread2(self):
            """STAR File read2 check"""
            # Freely available on the web so not included in package.
            entry = '1edp'
#            entry = '1q56'
            urlLocation = "http://www.bmrb.wisc.edu/WebModule/MRGridServlet?block_text_type=3-converted-DOCR&file_detail=3-converted-DOCR&pdb_id=%s&program=STAR&request_type=archive&subtype=full&type=entry" % (entry)
            fnamezip = entry+".zip"
            print "DEBUG: downloading url:", urlLocation
            urllib.urlretrieve(urlLocation,fnamezip)
            print "DEBUG: opening local zip file:", fnamezip
            zfobj = zipfile.ZipFile(fnamezip)
            fname = None
            for name in zfobj.namelist():    
                if name.endswith('.str'):
                    fname = name
            self.assertTrue(fname)
                
            fnameLocal = entry+".str"
            print "DEBUG: materializing file", fname, "as local STAR file:", fnameLocal
            outfile = open(fnameLocal, 'w')
            outfile.write(zfobj.read(fname))
            outfile.close()
            strf = File()                
            strf.filename  = fnameLocal
                
            def myfunc():
                start = time.time()
                print "DEBUG: reading file:", strf.filename
                if strf.read():
                    print "ERROR: In read. Exiting program"
                elapsed = time.time()-start
                print "took: %.3f seconds" % (elapsed)
        
        #    profile.run( 'myfunc()' )
            myfunc()
                                              
if __name__ == "__main__":
    unittest.main()