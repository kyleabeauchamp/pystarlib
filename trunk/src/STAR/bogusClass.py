'''
Created on Jun 24, 2011

@author: jd
'''
from nose.plugins.skip import SkipTest

try:
    import a.b.c #@UnusedImport @UnresolvedImport
except:
    raise SkipTest('bogusClass')

bogusParameter =1
