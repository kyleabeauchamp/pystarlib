'''
Used for testing the way SkipTest Exceptions can be thrown and handled by nose.
'''
from STAR.Utils import MySkipTest

try:
    import a #IGNORE:W0611 #IGNORE:F0401 #@UnusedImport @UnresolvedImport 
except:
    raise MySkipTest('bogusClass')

bogusParameter =1



