# Adding each component individually to PYTHONPATH
setenv PYSTARLIB_VARS $PYSTARLIB_ROOT/src

if ($?PYTHONPATH) then
    setenv PYTHONPATH ${PYSTARLIB_VARS}:${PYTHONPATH}
else
    setenv PYTHONPATH ${PYSTARLIB_VARS}
endif

rehash
