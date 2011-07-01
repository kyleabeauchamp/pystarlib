#@PydevCodeAnalysisIgnore 
'testing the pydev and pylint code analyses'
# pylint: disable=C0111 
# Above will cause pylint to ignore the lack of documentation here.
# Notee that for pydev code analysis the whole file can get ignored.
 
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
