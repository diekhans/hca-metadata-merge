metadata-merge = ../bin/metadata-merge

all:

test: 1m-neurons_test

1m-neurons_test: mkdirs
	${metadata-merge} input/1m-neurons output/$@.metadata.json

mkdirs:
	mkdir -p output

clean:
	rm -rf output
