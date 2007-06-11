import sys, unittest

"""
Call by:
python testAll.py
"""
if __name__ == "__main__":
    modList = ( 
               "STAR.TextTest", 
               "STAR.UtilsTest", 
               "STAR.TagTableTest", 
               "STAR.SaveFrameTest", 
               "STAR.FileTest", 
               )
    for mod_name in modList:
        print "Importing ", mod_name
        exec("import %s" % (mod_name,))
        exec("suite = unittest.defaultTestLoader.loadTestsFromModule(%s)" % (mod_name,))
        print "Testing"
        unittest.TextTestRunner(verbosity=2).run(suite)
