[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003150.svg)](https://doi.org/10.5281/zenodo.1003150) [![Build Status](https://travis-ci.org/citation-file-format/citation-file-format.github.io.svg?branch=src)](https://travis-ci.org/citation-file-format/citation-file-format.github.io) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# citation-file-format.github.io

## This repository holds the website and specifications for CFF

Documentation is provided in the form of a Jekyll site hosted on GitHub pages (using https://mmistakes.github.io/minimal-mistakes/), and a PDF.

### Versions

To work on a new version, create a branch from `src` with the version number,
e.g., `0.9-RC1`, create a directory named after the version, e.g., `0.9-RC1`,
and copy the `specifications.md` file from the last version into the directory.

**Important**: Do NOT *rename* the file, do NOT *change the directory structure*.

Specifications are only written in `specifications.md` in a version branch!
The Markdown dialect is [kramdown](https://kramdown.gettalong.org/), and
[Jekyll](https://jekyllrb.com/) specificities apply.

Once a version is release-ready, do the following:

- Create a landing page `index.md` file for the version in the `{version}` folder, describing the version (including release notes, changes, etc.).
- In `_config.yml`, set `current` to the version number, e.g., `0.9-RC1`.
- Add the version to the table in [versions.md](https://github.com/citation-file-format/citation-file-format.github.io/blob/src/versions.md).
- Merge the version branch to `src`.
- Push `src`. Travis CI will pick up the pushed commit and [build](#build) it. If you don't want your commits to be built automatically, add `[skip ci]` to your commit message.

### Build

At the moment, the build process is a bit of a monster, which will hopefully change once
[Pandoc 2.0.0](https://github.com/jgm/pandoc/milestone/4) is available.
At the moment, this is how CFF rolls:

1. The Jekyll site is created as per usual (`bundle exec jekyll build`)
2. A custom Pandoc build (on commit [181d737](https://github.com/jgm/pandoc/comm
it/181d7370bb913a0a9a110b2ae230a079f0c23be1) on the main [Pandoc
repo](https://github.com/jgm/pandoc)) is installed (for which the [Haskell Tool
Stack](https://docs.haskellstack.org/en/stable/README/) needs to be installed
first, etc.), as it handles multiline tables correctly (for conversion to PDF)
3. A [Python script](https://github.com/citation-file-format/citation-file-format.github.io/blob/src/build-pdfs.py) 
is invoked,  which uses regex (heavily) to get rid of kramdown-specific syntax,
Liquid tags, and unwanted things and converts everything from
`specifications.ms` to Pandoc markdown (and then does some more stuff on the
temporary Pandoc markdown) with the cusomt Pandoc installation, which is finally
used to build the PDF (complete with TOC, bibliography, formatted date, custom
LaTeX template, etc.).