metadata_merge = ../bin/metadata-merge
metadata_consume = ../bin/metadata-consume
cmp_metadata_representations = ../tests/bin/cmp-metadata-representations
projects_root = ../../../metadata-download/projects

project_dirs = $(wildcard ${projects_root}/*-*-*)
project_uuids = $(notdir ${project_dirs})

outdir = output
copy_dir = copy
sanity_dir = sanity

all:  demos

demos:  ${project_uuids:%=${outdir}/%.metadata.json} \
	${project_uuids:%=${copy_dir}/%.metadata.copy.json} \
	${project_uuids:%=${sanity_dir}/%.sanity.diff}

${outdir}/%.metadata.json:
	@mkdir -p $(dir $@)
	${metadata_merge} ${projects_root}/$* $@.tmp
	mv -f $@.tmp $@

# a couple sanity check of results
${copy_dir}/%.metadata.copy.json: ${outdir}/%.metadata.json
	@mkdir -p $(dir $@)
	${metadata_consume} $< $@.tmp
	diff $< $@.tmp
	mv -f $@.tmp $@


${sanity_dir}/%.sanity.diff: ${outdir}/%.metadata.json
	@mkdir -p $(dir $@)
	${cmp_metadata_representations} ${projects_root}/$* $< > $@.tmp
	mv -f $@.tmp $@

clean:
	rm -rf ${outdir} ${sanity_dir} ${copy_dir}
