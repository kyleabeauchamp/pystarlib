"""
Just a few utilities that can be of more general use.
"""
from nose.plugins.skip import SkipTest
import os
import re
import shutil

#pylint: disable=R0903
class Lister: #pylint: disable=W0232 
    """Example from 'Learning Python from O'Reilly publisher'"""
    def __repr__(self):
        return ("<Instance of %s, address %s:\n%s>" %
           (self.__class__.__name__, id(self), self.attrnames()))

    def attrnames(self):
        'Return a formatted representation of the attributes'
        result=''
        keys = sorted(self.__dict__.keys())
        for attr in keys:
            if attr[:2] == "__":
                result = result + "\tname %s=<built-in>\n" % attr
            else:
                result = result + "\tname %s=%s\n" % (attr, self.__dict__[attr])
        return result        

class MySkipTest(SkipTest):
    '''
    Subclassing so this dependency only occurs in one place of the code corpus.
    '''
# end class


def transpose ( matrix ):
    """
    A fast transposing algorithm from the python mailing list
    Used in TagTable.
    """
    if len( matrix ) < 1:
        print 'ERROR: trying to transpose an empty matrix'
        return 1
    elif len( matrix ) == 1:
        if len(matrix[0]) == 0:
            print 'ERROR: trying to transpose an empty matrix, shape would be lost'
            print 'ERROR: [[]] would become []'
            return 1
        else:
            return map( lambda y : (y,), matrix[0] )
    else:
        return apply( map, [None,] + list(matrix) )


def equalIgnoringWhiteSpace( a, b):
    """
    Collapses all whitespace to a single regular space
    before comparing. Doesn't remove final eol space.
    """
    pattern   = re.compile("\s+" )
    a = re.sub(pattern, ' ', a)
    b = re.sub(pattern, ' ', b)
#    print "a["+a+"]"
#    print "b["+b+"]"
    return a == b

def dos2unix(text):
    'Converts DOS line ends to Unix'
    return re.sub('\r\n', '\n', text)
def unix2dos(text):
    'Converts Unix line ends to DOS'
    return re.sub('([^\r])(\n)', '\1\r\n', text)
def mac2unix(text):
    'Converts Mac line ends to Unix'
    return re.sub('\r', '\n', text)

# Stolen from macostools
EEXIST  =   17  #File exists
def mkdirs(dst):
    """Make directories leading to 'dst' if they don't exist yet"""
    if dst == '' or os.path.exists(dst):
        return
    head, _tail = os.path.split(dst)
    if os.sep == ':' and not ':' in head:
        head = head + ':'
    mkdirs(head)

    try:
        os.mkdir(dst, 0777)
    except OSError, e:
        # be happy if someone already created the path
        if e.errno != EEXIST:
            raise
        # end if
    # end try
# end def

def rmdir(path):
    'DELETE AN ENTIRE DIRECTORY INCLUDING ALL THE FILES'
    if (os.path.exists(path)): 
        shutil.rmtree(path, 1)
