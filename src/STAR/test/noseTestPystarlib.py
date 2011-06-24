'''
Created on Jun 24, 2011

@author: jd
'''

import nose

# setup.cfg will be expected from cwd.
if nose.run():
    print "Nose ran fine"
else:
    print "ERROR: Nose failed"
    