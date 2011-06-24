clean:
	-/bin/rm -f .coverage nosetest.xml sloccount.sc

nose:
	# Write the .coverage and nosetest.xml
	# nosetests --with-xunit --with-coverage --verbose --cover-package=STAR --where=src/STAR
	nosetests --config=setup.cfg
	# Convert .coverage to coverage.xml
	coverage xml

pylint:
	cd src; pylint --rcfile .pylintrc STAR > pylint.txt || exit 0
	
sloccount:
	sloccount --duplicates --wide --details src > sloccount.sc