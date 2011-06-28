all: clean sloccount pylint nose

clean:
	-/bin/rm -f .coverage nosetest.xml sloccount.sc

	
sloccount:
	-/bin/rm -f sloccount.sc
	sloccount --duplicates --wide --details src > sloccount.sc
	
pylint:
	-/bin/rm -f src/pylint.txt
	cd src; pylint --rcfile ../.pylintrc STAR > pylint.txt || exit 0

nose:
	# Write the .coverage and nosetest.xml
	-/bin/rm -f .coverage nosetest.xml coverage.xml
	# nosetests --with-xunit --with-coverage --verbose --cover-package=STAR --where=src/STAR
	nosetests --config=setup.cfg
	# Convert .coverage to coverage.xml
	coverage xml

