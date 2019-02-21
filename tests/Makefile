metadata-merge = ../bin/metadata-merge
metadata-consume = ../bin/metadata-consume

all:

test: 1m-neurons_test mouse_melanoma_test fetal_maternal_test

# basic case
1m-neurons_test: mkdirs
	${metadata-merge} input/1m-neurons output/$@.metadata.json
	diff expected/$@.metadata.json output/$@.metadata.json
	${metadata-consume} output/$@.metadata.json output/$@.metadata.copy.json
	diff expected/$@.metadata.json output/$@.metadata.copy.json
	bin/cmp-metadata-representations input/1m-neurons output/$@.metadata.json > output/$@.sanity.diff

# cases with supplemental files
mouse_melanoma_test: mkdirs
	${metadata-merge} input/mouse_melanoma output/$@.metadata.json
	diff expected/$@.metadata.json output/$@.metadata.json
	${metadata-consume} output/$@.metadata.json output/$@.metadata.copy.json
	diff expected/$@.metadata.json output/$@.metadata.copy.json
	bin/cmp-metadata-representations input/mouse_melanoma output/$@.metadata.json > output/$@.sanity.diff

# case with analysis metadata
fetal_maternal_test: mkdirs
	${metadata-merge} input/fetal_maternal output/$@.metadata.json
	diff expected/$@.metadata.json output/$@.metadata.json
	${metadata-consume} output/$@.metadata.json output/$@.metadata.copy.json
	diff expected/$@.metadata.json output/$@.metadata.copy.json
	bin/cmp-metadata-representations input/fetal_maternal output/$@.metadata.json > output/$@.sanity.diff

mkdirs:
	mkdir -p output

clean:
	rm -rf output
