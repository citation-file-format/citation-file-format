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

- The build is set up through [.travis.yml](https://github.com/citation-file-format/citation-file-format.github.io/blob/src/.travis.yml): 
  - Python version: 3.6
  - `apt-get` installations:
    - `texlive-full`
    - `pandoc`
    - `pandoc-citeproc`
  - `pip` installations:
    - pypandoc
    - pandoc-frontmatter
  - Build script: [`travis-build.sh`](https://github.com/citation-file-format/citation-file-format.github.io/blob/src/travis-build.sh), which does the following:

1. Install the [Haskell Tool Stack](https://docs.haskellstack.org/en/stable/README/)
2. Use `stack` to install a custom version of Pandoc, which is needed to enforce multiline tables (commit 
[181d737](https://github.com/jgm/pandoc/commit/181d7370bb913a0a9a110b2ae230a079f0c23be1) on the main [Pandoc
repo](https://github.com/jgm/pandoc))
3. Clone the existing site from `master`
4. Run a [Python script](https://github.com/citation-file-format/citation-file-format.github.io/blob/src/build-pdfs.py) 
which works on temporary copies of all `specifications.md` files (replace *kramdown*-specific citation syntax with Pandoc
syntax; remove "Download PDF" button; remove Liquid CSS style tags; remove Liquid TOC inclusion tag; replace Liquid
version tag with real tag (from parent directory name); remove Liquid bibliography tag; remove Zenodo DOI badge;
fix links to GitHub user handles; build PDFs with custom Pandoc version for each specs file and copy it to the
*assets* directory where it will be picked up by Jekyll)
5. Build the Jekyll site
6. Push the *_site* directory (i.e. the build target) back to `master`
