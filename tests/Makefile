metadata2tsv = ../bin/metadata2tsv

all:

test: 1m-neurons_tests

1m-neurons_tests: mkdirs
	${metadata2tsv} input/1m-neurons/

mkdirs:
	mkdir -p output

clean:
	rm -rf output
