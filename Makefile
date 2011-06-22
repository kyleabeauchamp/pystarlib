# jfd 2011-06-17
		
#sloccount:
#	sloccount --duplicates --wide --details divergence/*.py divergence/test/*.py > sloccount.sc

nose:
	nosetests --with-xunit --with-coverage --verbose --cover-package=STAR --where=src/STAR
#	nosetests --testmatch=test_.+.py
	coverage xml

pylint:
#	pylint --max-line-length=120 --disable="E0602,W0511" -f parseable --include-ids=y STAR > pylint.txt || exit 0
	cd src; pylint --rcfile .pylibrc STAR > pylint.txt || exit 0