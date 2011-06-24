#!/bin/tcsh -e

# Used by Jenkins to build and test this installation automatically on various platforms. 

cd $0:h

echo "DEBUG: PATH       1: $PATH"
echo "DEBUG: PYTHONPATH 1: $PYTHONPATH"

setenv PYSTARLIB_ROOT $cwd
source pystarlib.csh

echo "DEBUG: PATH       2  : $PATH"
echo "DEBUG: PYTHONPATH 2  : $PYTHONPATH"

# Comment out the next line after done testing for it's a security issue.
#setenv | sort

make clean
make nose
make pylint
make sloccount

echo "Done"
