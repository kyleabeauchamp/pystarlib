"""
Just a few utilities that can be of more general use.
"""
import os
import re
import shutil

__author__    = "$Author$"
___revision__ = "$Revision$"
___date__     = "$Date$"

"""
$Log$
Revision 1.2  2007/01/23 18:08:11  jurgenfd
The below quoted value wasn't parsed correctly.
Occurs in the MR file for entry 2ihx.

'#It has very upfield-shifted H5', H5" @ 3.935,4.012 ppm'

Fixed with this update.

Revision 1.1.1.1  2007/01/09 22:10:15  jurgenfd
initial import

Revision 1.1  2007/01/08 20:49:41  jurgen
Merged improvements from Wim Vranken (EBI) back in.

Revision 1.1.1.1  2001/11/02 20:16:40  jurgen
Initial package capable of read/write access to STAR files without nested loops

"""

class Lister:
    """Example from 'Learning Python from O'Reilly publisher'"""
    def __repr__(self):
        return ("<Instance of %s, address %s:\n%s>" %
           (self.__class__.__name__, id(self), self.attrnames()))

    def attrnames(self):
        result=''
        keys = sorted(self.__dict__.keys())
        for attr in keys:
            if attr[:2] == "__":
                result = result + "\tname %s=<built-in>\n" % attr
            else:
                result = result + "\tname %s=%s\n" % (attr, self.__dict__[attr])
        return result        


"""
A fast transposing algorithm from the python mailing list
Used in TagTable.
"""
def transpose ( matrix ):
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


"""
Collapses all whitespace to a single regular space
before comparing. Doesn't remove final eol space.
"""
def equalIgnoringWhiteSpace( a, b):
    pattern   = re.compile("\s+" )
    a = re.sub(pattern, ' ', a)
    b = re.sub(pattern, ' ', b)
#    print "a["+a+"]"
#    print "b["+b+"]"
    return a == b

def dos2unix(text):
    return re.sub('\r\n', '\n', text)
def unix2dos(text):
    return re.sub('([^\r])(\n)', '\1\r\n', text)
def mac2unix(text):
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

# DELETE AN ENTIRE DIRECTORY INCLUDING ALL THE FILES
# ==================================================
def rmdir(path):
    if (os.path.exists(path)): 
        shutil.rmtree(path, 1)
