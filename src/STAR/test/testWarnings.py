'''
Created on Jun 24, 2011

@author: jd
'''

print 'Before imports'

from warnings import warn

print 'Before first filter'
#simplefilter('ignore', category=UserWarning)
#warn('Listen up')

print 'Before filter 2'
#simplefilter('ignore', category=ImportWarning)
warn('Import away', ImportWarning) # Off by default.

print 'Before filter 3'
#raise ImportWarning('a fine warning')

print 'Done'
