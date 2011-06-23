nose:
	# Write the .coverage and nosetest.xml
	nosetests --with-xunit --with-coverage --verbose --cover-package=STAR --where=src/STAR
	# Convert .coverage to coverage.xml
	coverage xml

pylint:
	cd src; pylint --rcfile .pylibrc STAR > pylint.txt || exit 0
	
sloccount:
	sloccount --duplicates --wide --details src > sloccount.sc