'All unit checks available thru this one python script'
import unittest

modList = ( 
           "STAR.test.test_Text", 
           "STAR.test.test_Utils", 
           "STAR.test.test_TagTable", 
           "STAR.test.test_SaveFrame", 
           "STAR.test.test_File", 
           )
# Next line is to fool pydev extensions into thinking suite is defined in the regular way.
suite = None
for mod_name in modList:
    print "Importing ", mod_name
    exec("import %s" % (mod_name,))
    exec("suite = unittest.defaultTestLoader.loadTestsFromModule(%s)" % (mod_name,))
    print "Testing"
    unittest.TextTestRunner(verbosity=2).run(suite)
