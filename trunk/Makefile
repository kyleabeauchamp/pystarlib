nose:
	nosetests --with-xunit --with-coverage --verbose --cover-package=STAR --where=src/STAR
	coverage xml

pylint:
	cd src; pylint --rcfile .pylibrc STAR > pylint.txt || exit 0
	
sloccount:
	sloccount --duplicates --wide --details  src > sloccount.sc
