[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003150.svg)](https://doi.org/10.5281/zenodo.1003150) [![Build Status](https://travis-ci.org/citation-file-format/citation-file-format.github.io.svg?branch=src)](https://travis-ci.org/citation-file-format/citation-file-format.github.io) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# Citation File Format (CFF) Specifications

The format specifications for CFF are available online and as a PDF here: <https://citation-file-format.github.io/>.


# citation-file-format.github.io

For general information (contributing, other repositories, etc.), please see https://github.com/citation-file-format/citation-file-format/blob/master/README.md.

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

- Create a landing page `{version}.md` file for the version in the `{version}` folder, describing the version (including release notes, changes, etc.).
- In `_config.yml`, set `current` to the version number, e.g., `0.9-RC1`.
- Add the version to the table in [versions.md](https://github.com/citation-file-format/citation-file-format.github.io/blob/src/versions.md).
- Add the version in the PDF link to deploy in .travis.yml
- Commit the changes
- Run changes.sh to create a list of changes to display on the landing page
- Merge the version branch to `src`.
- Push `src`. Travis CI will pick up the pushed commit and [build](#build) it. If you don't want your commits to be built automatically, add `[skip ci]` to your commit message.

### Build

- Push `src` to GitHub, Travis will take care of the rest