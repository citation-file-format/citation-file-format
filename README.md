# Citation File Format (CFF)

[![Build Status](https://github.com/citation-file-format/citation-file-format/workflows/testing/badge.svg)](https://github.com/citation-file-format/citation-file-format/actions/workflows/testing.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003149.svg)](https://doi.org/10.5281/zenodo.1003149)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

The Citation File Format specifies how users can provide citation metadata for software or datasets that is easy to read by humans as well as by machines.

## Structure

`CITATION.cff` files in the Citation File Format consist of three parts:

1. The **software** (or dataset) **citation metadata** - as the most important part, this is **required**.
2. A **references** section - works like a references section in a paper, so that you can give credit to the authors of works that your software or dataset builds on.
3. One **preferred citation** - so that even when you ask people to cite your software or dataset, they can also additionally cite a traditional paper.

### Example

This is what a common `CITATION.cff` file for research software may look like:

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

## Format specifications :books:

You can find the complete format specifications in the [Guide to the Citation File Format schema](schema-guide.md).

## Why should I add a `CITATION.cff` file to my repository? :bulb:

When you do this, great things may happen:

1. People that find your software can easily cite it using the correct metadata from `CITATION.cff`!
2. If your repository is hosted on GitHub, [they will link to it](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files) in a special "Cite this repository" widget on the repository landing page. Also, the citation information in `CITATION.cff` will be used when you publish your software on Zenodo via the [GitHub-Zenodo bridge](https://guides.github.com/activities/citable-code/).
3. The citation information in `CITATION.cff` can be used by the open source reference manager [Zotero](https://github.com/zotero/zotero), when people import the repository.

## Validation :heavy_check_mark:

## Tools to work with `CITATION.cff` files :wrench:

## Maintainers :nerd_face:

The Citation File Format schema is maintained by

- [Stephan Druskat](https://sdruskat.net) ([@sdruskat](https://github.com/sdruskat/))
- Jurriaan Spaaks ([@jspaaks](https://github.com/jspaaks/))

## Contributing :handshake:

**The _Citation File Format_ is a collaborative project** and we welcome suggestions and contributions. We hope one of the invitations below works for you, but if not, please let us know!

:running: **I'm busy, I only have 1 minute**
- Tell a friend about the *Citation File Format*!

:hourglass_flowing_sand: **I've got 5 minutes - tell me what I should do**
- Create a `CITATION.cff` file for your repository.
- Suggest ideas for how you would like to use the *Citation File Format*, or for an improvement to the format or its tooling.

:computer: **I've got a few hours to work on this**
- Take a look at the issues and see if there are any you can contribute to.

:tada: **I really want to help increase the community**
- Organise a hack event or workshop to help others use or improve the *Citation File Format*.

Please read the more detailed [contributing guidelines](CONTRIBUTING.md) and [open a GitHub issue](https://github.com/citation-file-format/citation-file-format/issues) to suggest a new idea or let us know about bugs.

## License :balance_scale:

Copyright © 2016ff. The Citation File Format Contributors

This work is licensed under multiple licenses:
- The schema ([`schema.json`](schema.json)) is licensed under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/legalcode).
- The schema guide ([`schema-guide.md`](schema-guide.md)) is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).
- Insignificant files are licensed under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

## Acknowledgments :pray:

**We'd like to thank everyone who has contributed to the Citation File Format!**  
They are listed in the [`CITATION.cff`](CITATION.cff) file for this repository. Please open an issue if you find that you are missing from the file.

We gratefully acknowledge support from:

- The [Institute for Software Technology](https://www.dlr.de/sc/en/desktopdefault.aspx/) of the [German Aerospace Center (DLR)](https://www.dlr.de/en/)
- The [Netherlands eScience Center](https://www.esciencecenter.nl/)
- The [Software Sustainability Institute](https://software.ac.uk/)
