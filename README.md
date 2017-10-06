[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003150.svg)](https://doi.org/10.5281/zenodo.1003150) [![Build Status](https://travis-ci.org/sdruskat/citation-file-format.svg?branch=master)](https://travis-ci.org/sdruskat/citation-file-format) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# Citation File Format (CFF)

## Format specifications for `CITATION` files. `CITATION` files provide citation metadata for (research/scientific) software.

### **Read the current version of the specifications**: [online](http://sdruskat.github.io/citation-file-format) | [PDF](http://sdruskat.github.io/citation-file-format/assets/pdf/cff-specifications.pdf).

---

This branch holds the files to build a Jekyll site for GitHub Pages via Jekyll.

### Build

Build the specifications PDF with [the build script `build.sh`](https://github.com/sdruskat/citation-file-format/blob/master/build.sh).

Jekyll site build via Travis and [`build-jekyll.sh`](https://github.com/sdruskat/citation-file-format/blob/master/build-jekyll.sh).

## Work on the specs

The current specs are **exclusively** held in the `index.md` file in the root of this branch. Other `index.md` files in nested directories contain older versions of the specs and **must not be changed**.

## Create a new version / archive old versions

1. Create a directory for the current version as documented in `./index.md`. E.g., if the current version is 1.0.0, create a directory `1.0.0` and copy `./index.md` to that directory.
2. Set up `./index.md` for the new version by changing `version` in the metadata accordingly, e.g., to `1.0.1`.

## Release

Before a release, make sure to build the lates version PDF locally with `build.sh`, otherwise an old version will end up in the release archive on GitHub.