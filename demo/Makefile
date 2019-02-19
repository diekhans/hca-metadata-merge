metadata-merge = ../bin/metadata-merge

projects_root = ../../../metadata-download/projects

project_dirs = $(wildcard ${projects_root}/*-*-*)
project_uuids = $(notdir ${project_dirs})

outdir = output

all:  demos

demos: ${project_uuids:%=${outdir}/%.metadata.json}

${outdir}/%.metadata.json:
	@mkdir -p $(dir $@)
	${metadata-merge} ${projects_root}/$* $@.tmp
	#mv -f $@.tmp $@

clean:
	rm -rf ${outdir}
