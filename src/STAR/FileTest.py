"""Unit test
"""
    
import zipfile
import urllib
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

'#It has very upfield-shifted H5', H5" @ 3.935,4.012 ppm'
;
#######################
#  BOGUS              #
#######################

;
        
    BOGUS_CATEGORY

     stop_
save_
"""
            self.assertFalse(self.strf.parse(text=text))                                    
            st = self.strf.star_text()
#            print "unparsed text:[" +st+ "]"

            exp = """data_no_comments_here
save_comment   _Saveframe_category  comment   loop_
        _comment
        _every_flag
        _category
;#It has very upfield-shifted H5', H5" @ 3.935,4.012 ppm
;
;
#######################
#  BOGUS              #
#######################

;    BOGUS_CATEGORY     stop_ save_
"""
            self.assertTrue(Utils.equalIgnoringWhiteSpace(exp,st))

        def testread2(self):
            """STAR File read"""
            testEntry('1edp')
              
"""
Extra Test Routine going over some entries in the NMR Restraints Grid
"""
def testEntry(entry):
    strf = File() 
    STAR.verbosity = 2
    # Freely available on the web so not included in package.
    stage = "2-parsed"
#    stage = "3-converted-DOCR"
    urlLocation = ("http://www.bmrb.wisc.edu/WebModule/MRGridServlet?"+
    "block_text_type=%s&file_detail=%s&pdb_id=%s"+
    "&program=STAR&request_type=archive&subtype=full&type=entry") % (stage, stage, entry)
    fnamezip = entry+".zip"
#    print "DEBUG: downloading url:", urlLocation
    urllib.urlretrieve(urlLocation,fnamezip)
#    print "DEBUG: opening local zip file:", fnamezip
    zfobj = zipfile.ZipFile(fnamezip)
    fname = None
    for name in zfobj.namelist():    
        if name.endswith('.str'):
            fname = name            
    fnameLocal = entry+".str"
#    print "DEBUG: materializing file", fname, "as local STAR file:", fnameLocal
    outfile = open(fnameLocal, 'w')
    outfile.write(zfobj.read(fname))
    outfile.close()      
    zfobj.close()          
    strf.filename  = fnameLocal   
        
#    print "DEBUG: parsing file"
    strf.read()
#    print "DEBUG: writing file"
    strf.filename  = strf.filename + "_new.str"
    strf.write()

    # In order to make the tests below work you'll first need to install Wattos
    #  which is why this test is not standard.
    wattosInstalled = 0
    if wattosInstalled:
        print "DEBUG: rewrite to Java formating for comparison"
        cmd = "java -Xmx256m Wattos.Star.STARFilter %s %s ." % ( strf.filename, entry+"_r.str")
        os.system(cmd)
        diffInstalled = 0
        if diffInstalled:
            print "DEBUG: diffing"
            cmd = "diff -w %s %s > %s" % ( entry+".str", entry+"_r.str", entry+"_diff.txt")
            os.system(cmd)

#    print "DEBUG: cleaning up files"
    os.unlink(strf.filename)
    os.unlink(entry+".zip")
#    os.unlink(entry+".str")
#    os.unlink(entry+"_r.str")
#    os.unlink(entry+"_diff.str")
    
    
def testAllEntries():
    pdbList = ('1edp', '1q56', '1brv', '2hgh')
    try:
        from Wattos.Utils import PDBEntryLists
        print "Imported Wattos.Utils; but it's not essential"
        pdbList = PDBEntryLists.getBmrbNmrGridEntries()[0:4] # Decide on the range yourself.
    except:
        print "Skipping import of Wattos.Utils; it's not needed"
    
    for entry in pdbList:
        print entry
        testEntry(entry)
#        entry = '1edp' # 57 kb
    #    entry = '1q56' # 10 Mb takes 27 s to parse on 2GHz PIV CPU
    #    entry = '1brv' # 1 Mb 
    #    entry = '1hue' # 6 Mb takes 26 s to parse on 2GHz PIV CPU
    #    entry = '2ihx' # ? Mb has weird quoted values
    
"""
Extra Test Routine going over some entries in the NMR Restraints Grid
"""
def testSingleFile( filename ):
    strf = File() 
    strf.filename  = filename   
    print "DEBUG: reading file ", strf.filename
    strf.read()
    strf.filename  = strf.filename + "_new.str"
    print "DEBUG: writing file ", strf.filename
    strf.write()
    
        
if __name__ == "__main__":
    testAllEntries()
#    testSingleFile("S:\\jurgen\\2hgh_small_new_google.str")
    unittest.main()
    print "Done with STAR.FileTest"