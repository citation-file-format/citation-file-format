# Citation File Format

[![Build Status](https://github.com/citation-file-format/citation-file-format/workflows/testing/badge.svg)](https://github.com/citation-file-format/citation-file-format/actions/workflows/testing.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003149.svg)](https://doi.org/10.5281/zenodo.1003149)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Project homepage](https://img.shields.io/badge/Project%20homepage-citation--file--format.github.io-ff0080)](https://citation-file-format.github.io)

The Citation File Format lets you provide citation metadata for software or datasets 
in plaintext files that are easy to read by both humans and machines.

## Structure

You can specify citation metadata for your software (or dataset) in a file named `CITATION.cff`.

This is what a typical `CITATION.cff` file for research software may look like:

```yaml
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
title: My Research Software
abstract: This is my awesome research software. It does many things.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: "https://orcid.org/0000-0003-4925-7248"
version: 0.11.2
date-released: "2021-07-18"
identifiers:
  - description: This is the collection of archived snapshots of all versions of My Research Software
    type: doi
    value: "10.5281/zenodo.123456"
  - description: This is the archived snapshot of version 0.11.2 of My Research Software
    type: doi
    value: "10.5281/zenodo.123457"
license: Apache-2.0
repository-code: "https://github.com/citation-file-format/my-research-software"
```

In addition, the Citation File Format allows you to

- provide references to works that your software or dataset builds on ([see here for more info](schema-guide.md#referencing-other-work));
- ask people to cite a different, related work instead of the software or dataset itself ([see here for more info](schema-guide.md#credit-redirection)).

## Format specifications :books:

You can find the complete format specifications in the [Guide to the Citation File Format schema](schema-guide.md).

## Why should I add a `CITATION.cff` file to my repository? :bulb:

When you do this, great things may happen:

1. People that find your software can easily cite it using the correct metadata from `CITATION.cff`!
2. If your repository is hosted on GitHub, they will [show the citation information in the sidebar](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files), which makes it easy for visitors to cite your software or dataset correctly.
3. When you publish your software on Zenodo via the [GitHub-Zenodo integration](https://guides.github.com/activities/citable-code/), they will use the metadata from your `CITATION.cff` file.
4. People can import the correct reference to your software into the [Zotero](https://www.zotero.org) reference manager via a [browser plugin](https://www.zotero.org/download/).

## Validation :heavy_check_mark:

## Tools to work with `CITATION.cff` files :wrench:

## Maintainers :nerd_face:

The Citation File Format schema is maintained by

- Stephan Druskat ([@sdruskat](https://github.com/sdruskat/))
- Jurriaan H. Spaaks ([@jspaaks](https://github.com/jspaaks/))

## Contributing :handshake:

The Citation File Format is a collaborative project and we welcome suggestions and contributions. We hope one of the invitations below works for you, but if not, please let us know!

:running: **I'm busy, I only have 1 minute**
- Tell a friend about the Citation File Format, or tweet about it!

:hourglass_flowing_sand: **I've got 10 minutes - tell me what I should do**
- Create a `CITATION.cff` file for your repository.
- Suggest ideas for how you would like to use the Citation File Format, or for an improvement to the format or its tooling.

:computer: **I've got a few hours to work on this**
- Take a look at the issues and see if there are any you can contribute to.

:tada: **I want to help increase the community**
- Write a blog post or news item for your own community.
- Organise a hack event or workshop to help others use or improve the Citation File Format.

Please read the more detailed [contributing guidelines](CONTRIBUTING.md) and [open a GitHub issue](https://github.com/citation-file-format/citation-file-format/issues) to suggest a new idea or let us know about bugs.

## License :balance_scale:

Copyright © 2016ff. The Citation File Format Contributors

This work is licensed under a [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/legalcode) license.

## Acknowledgments :pray:

**We'd like to thank everyone who has contributed to the Citation File Format!**  
They are listed in the [`CITATION.cff`](CITATION.cff) file for this repository. Please open an issue if you find that you are missing from the file.

We gratefully acknowledge support from:

- The [Institute for Software Technology](https://www.dlr.de/sc/en/desktopdefault.aspx/) of the [German Aerospace Center (DLR)](https://www.dlr.de/en/)
- The [Netherlands eScience Center](https://www.esciencecenter.nl/)
- The [Software Sustainability Institute](https://software.ac.uk/)
