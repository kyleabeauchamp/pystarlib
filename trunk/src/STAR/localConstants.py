"""
Only localizations needed
"""
import os

# Only need to specify once when developping on only one os.
dir         = '/share'
if os.name == 'nt': # Windows drives
    dir         = os.path.join('C:\\','Documents and Settings','jurgen.WHELK.000','workspace')
    
StarCodeDir       = os.path.join(dir,'STAR','src','STAR')
TestDataDir       = os.path.join(dir,'STAR','test_data')
#print StarCodeDir
print "Read STAR.localConstants.py version 0.2.0"