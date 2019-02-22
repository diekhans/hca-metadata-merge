

all:

test:
	cd tests && ${MAKE} test


clean:
	cd tests && ${MAKE} clean
	cd demo && ${MAKE} clean

demo:
	cd demo && ${MAKE} demo

lint:
	python3 -m flake8 bin/metadata-merge bin/metadata-consume bin/mb_support.py

