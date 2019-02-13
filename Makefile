

all:

test:
	cd tests && ${MAKE} test


clean:
	cd tests && ${MAKE} clean


lint:
	python3 -m flake8 bin/metadata2tsv
