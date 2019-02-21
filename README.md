# hca-metadata-merge
Prototype code to generate combined metadata JSON files.


## Description

The program ```bin/metadata-merge``` takes the metadata from all of the
bundles, de-duplicates it and create a single file with the array of all the
metadata entities.  This requires each bundle is required to contain a
```bundle.json``` file, which is not normally part of a download and must be
created with the ```hca dss get-bundle``` command.

This implementation makes non-schema compliant modifications to the JSON to
simplify graph reconstruction my removing the need to combine links.json and
the bundle manifest to reconstruct the graph.

The following modifications have made:

- Each metadata entity has the fields ```provenance.document_version``` and
  ```provenance.document_fqid```

- The DAG is described by adding the fields ```provenance.inputs```, which is a
  list of fqids. This allows the DAG to be constructed by a 
  bottom-up traversal.  Forward links are not possible, as that would change the
  version of the entity any time something is derived from it.  These are not added
  to the ```protocol``` entities.
  
- Process entities have ```provenance.protocols``` added as a list of fqids.

- The links.json file has no provenance information and is incapable of
  handling multiple versions without some redesign, so it is not include on
  the first pass.

Writing this program  has lead to the discovery that, if there were multiple versions of
metadata entities in a project, it would be very difficult to build the various
version graphs.

## Examples
Due to github size limits, the sample ```metaata.json``` files are under:

<https://hgwdev.gi.ucsc.edu/~markd/hca/metadata-merge/>

## Issues
- Entity fqids are not currently used everywhere in the code, this will report errors if there is a problem.
- The links.json structure seems hard to impossible to use when multiple versions are supported
- supplementary files are not linked into metadata graph in any way and their detection.
