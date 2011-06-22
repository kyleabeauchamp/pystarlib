# Adding each component individually to PYTHONPATH
setenv  PYSTARLIB_VARS $PYSTARLIB_ROOT/python

if ($?PYTHONPATH) then
    setenv PYTHONPATH ${PYSTARLIB_VARS}:${PYTHONPATH}
else
    setenv PYTHONPATH ${PYSTARLIB_VARS}
endif

rehash
