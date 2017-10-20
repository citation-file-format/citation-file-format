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

- Build the PDF files locally by running build-pdfs.py (works with Python 3.6, needs `pypandoc`, `pandoc-frontmatter`, a custom pandoc build from commit [181d737](https://github.com/jgm/pandoc/commit/181d7370bb913a0a9a110b2ae230a079f0c23be1) on the main [Pandoc
repo](https://github.com/jgm/pandoc), `pandoc-citeproc` v >= 0.10.3)
- Push, Travis will take care of the rest