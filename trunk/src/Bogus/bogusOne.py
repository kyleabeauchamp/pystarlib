#@PydevCodeAnalysisIgnore # pylint: disable-all
'''
Created on Jun 29, 2011

@author: jd
'''


x = a # this is a bug. Detectable by pydev but not by pylint. 
error 

#The next line would cause a pylint info message but because of the above pylint directive it and any other error will be ignore.
y = "A very long line indeed ....................................................................................................................."

