# Citation File Format

[![Build Status](https://github.com/citation-file-format/citation-file-format/actions/workflows/testing.yml/badge.svg?branch=main)](https://github.com/citation-file-format/citation-file-format/actions/workflows/testing.yml?query=branch%3Amain)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003149.svg)](https://doi.org/10.5281/zenodo.1003149)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Project homepage](https://img.shields.io/badge/Project%20homepage-citation--file--format.github.io-ff0080)](https://citation-file-format.github.io)

The Citation File Format lets you provide citation metadata for software or datasets 
in plaintext files that are easy to read by both humans and machines.

## Structure

You can specify citation metadata for your software (or dataset) in a file named `CITATION.cff`. 
This is what a typical `CITATION.cff` file may look like for research software:

```yaml
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
title: My Research Software
abstract: This is my awesome research software. It does many things.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: "https://orcid.org/1234-5678-9101-1121"
  - name: "The Research Software project"
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

**You can find the complete format specifications in the [Guide to the Citation File Format schema](schema-guide.md).**

## Why should I add a `CITATION.cff` file to my repository? :bulb:

When you do this, great things may happen:

1. Users of your software can easily cite it using the metadata from `CITATION.cff`!
2. If your repository is hosted on GitHub, they will [show the citation information in the sidebar](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files), which makes it easy for visitors to cite your software or dataset correctly.
3. When you publish your software on Zenodo via the [GitHub-Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content), they will use the metadata from your `CITATION.cff` file.
4. People can import the correct reference to your software into the [Zotero](https://www.zotero.org) reference manager via a [browser plugin](https://www.zotero.org/download/).

## Creation :heavy_plus_sign:

To create a `CITATION.cff` file, you can 

- use the [**cffinit** website](https://citation-file-format.github.io/cff-initializer-javascript/#/),
- copy and paste the [example snippet](#structure), and adapt it to your needs, or
- create a new file called `CITATION.cff` using the *Add file* button on GitHub, and use the template they provide.

## Validation :heavy_check_mark:

You can validate your `CITATION.cff` file on the command line with the [`cffconvert` Python package](https://pypi.org/project/cffconvert/):

```shell
# Install cffconvert with pip in user space
python3 -m pip install --user cffconvert

# Validate your CFF file
cffconvert --validate
```

If you get a Traceback with error messages, look for the relevant validation error and fix it.
If the output is very long, it may help if you search it for lines starting with `jsonschema.exceptions.ValidationError`.

If you prefer to use Docker, you can use the [`cffconvert` Docker image](https://hub.docker.com/r/citationcff/cffconvert):

```bash
cd <directory-containing-your-CITATION.cff>
docker run --rm -v ${PWD}:/app citationcff/cffconvert --validate
```

<!-- Later, this should link to tutorials -->

## Tools to work with `CITATION.cff` files :wrench:

There is tooling available to work with `CITATION.cff` files to do different things:
create new files, edit existing files, validate existing files, convert files from the Citation File Format into another format.
The following table gives an overview of the tools that we know about. If there is a tool missing from this table, please [open a new issue](https://github.com/citation-file-format/citation-file-format/issues/new/choose) and let us know.

|                | Creation                                                                        | Editing/Updating                                                    | Validation                                                                      | Conversion                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Command line   |                                                                                 |                                                                     | • [cffconvert](#validation-heavy_check_mark)                                    | • [cffconvert](https://pypi.org/project/cffconvert/)<br> • [bibtex-to-cff](https://github.com/monperrus/bibtexbrowser/)<br>• [cff-from-621](https://pypi.org/project/cff-from-621/)<br>• [openCARP-CI](https://git.opencarp.org/openCARP/openCARP-CI/-/tree/master/#create_cff)                                                                                                                   |
| GitHub Actions |                                                                                 |                                                                     | [cff-validator](https://github.com/marketplace/actions/cff-validator)           | • [cffconvert](https://github.com/marketplace/actions/cffconvert)<br>• [codemeta2cff](https://github.com/caltechlibrary/codemeta2cff)                                                                                                                                                                                                                                                             |
| GitHub Bot     |                                                                                 |                                                                     | [#238](https://github.com/citation-file-format/citation-file-format/issues/238) |                                                                                                                                                                                                                                                                                                                                                                                                   |
| Docker         |                                                                                 |                                                                     | [cffconvert Docker image](#validation-heavy_check_mark)                         | [cffconvert Docker image](https://hub.docker.com/r/citationcff/cffconvert)                                                                                                                                                                                                                                                                                                                        |
| Go             |                                                                                 |                                                                     |                                                                                 | • [datatools/codemeta2cff](https://github.com/caltechlibrary/datatools/)                                                                                                                                                                                                                                                                                                                          |
| Haskell        |                                                                                 | • [cffreference](https://github.com/kevinmatthes/cffreference)      |                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                   |
| Java           | • [CFF Maven plugin](https://github.com/hexatomic/cff-maven-plugin)             | • [CFF Maven plugin](https://github.com/hexatomic/cff-maven-plugin) |                                                                                 | • [CFF Maven plugin](https://github.com/hexatomic/cff-maven-plugin)                                                                                                                                                                                                                                                                                                                               |
| JavaScript     |                                                                                 |                                                                     |                                                                                 | • [Citation.js](https://citation.js.org/) [plugin](https://www.npmjs.com/package/@citation-js/plugin-software-formats)                                                                                                                                                                                                                                                                            |
| Julia          |                                                                                 |                                                                     | • [Bibliography.jl](https://github.com/Humans-of-Julia/Bibliography.jl)         | • [Bibliography.jl](https://github.com/Humans-of-Julia/Bibliography.jl)                                                                                                                                                                                                                                                                                                                           |
| PHP            |                                                                                 |                                                                     |                                                                                 | • [bibtex-to-cff](https://github.com/monperrus/bibtexbrowser/)                                                                                                                                                                                                                                                                                                                                    |
| Python         |                                                                                 | • [cff2toml](https://github.com/willynilly/cff2toml)<br> • [doi2cff](https://github.com/citation-file-format/doi2cff)<br> • [updateCitation](https://github.com/hunterhogan/updateCitation) | • [cffconvert](#validation-heavy_check_mark)                                    | • [cff-from-621](https://pypi.org/project/cff-from-621/)<br>• [cff2toml](https://github.com/willynilly/cff2toml)<br>• [cffconvert](https://github.com/citation-file-format/cff-converter-python)<br>• [doi2cff](https://github.com/citation-file-format/doi2cff)<br>• [openCARP-CI](https://git.opencarp.org/openCARP/openCARP-CI/-/tree/master/#create_cff)<br>• [py_bibtex_to_cff_converter](https://github.com/vdplasthijs/py_bibtex_to_cff_converter) |
| R              |                                                                                 |                                                                     | • [cffr](https://CRAN.R-project.org/package=cffr)                                                                                | • [citation](https://cran.r-project.org/web/packages/citation/)<br>• [r2cff](https://github.com/ocbe-uio/RCFF)<br>• [handlr](https://github.com/ropensci/handlr)<br>• [cffr](https://CRAN.R-project.org/package=cffr)                                                                                                                                                                             |
| Ruby           | • [ruby-cff](https://github.com/citation-file-format/ruby-cff)                  | • [ruby-cff](https://github.com/citation-file-format/ruby-cff)      | • [ruby-cff](https://github.com/citation-file-format/ruby-cff)                  | • [ruby-cff](https://github.com/citation-file-format/ruby-cff)                                                                                                                                                                                                                                                                                                                                    |
| Rust           | • [Aeruginous](https://github.com/kevinmatthes/aeruginous-rs)                   | • [Aeruginous](https://github.com/kevinmatthes/aeruginous-rs)       |                                                                                 | • [citeworks](https://github.com/passcod/citeworks)                                                                                                                                                                                                                                                                                                                                               |
| TypeScript     |                                                                                 |                                                                     |                                                                                 | [#28](https://github.com/citation-file-format/citation-file-format/issues/28#issuecomment-892105342)                                                                                                                                                                                                                                                                                              |
| Website        | • [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) |                                                                     |                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                   |

## Maintainers :nerd_face:

The Citation File Format schema is maintained by

- Stephan Druskat ([@sdruskat](https://github.com/sdruskat/))
- Jurriaan H. Spaaks ([@jspaaks](https://github.com/jspaaks/))

## Contributing :handshake:

The Citation File Format is a collaborative project and we welcome suggestions and contributions. We hope one of the invitations below works for you, but if not, please let us know!

:running: **I'm busy, I only have 1 minute**
- Tell a friend about the Citation File Format, or tweet about it!
- Give the project a star :star:!

:hourglass_flowing_sand: **I've got 10 minutes - tell me what I should do**
- Create a `CITATION.cff` file for your repository.
- Suggest ideas for how you would like to use the Citation File Format, or for an improvement to the format or its tooling.
- If you know how to validate `CITATION.cff` files, help someone with a validation problem and look at the [issues labeled ![GitHub labels](https://img.shields.io/github/labels/citation-file-format/citation-file-format/validation)](https://github.com/citation-file-format/citation-file-format/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22+label%3Avalidation)

:computer: **I've got a few hours to work on this**
- Help create tooling for the community by looking at the [issues labeled ![GitHub labels](https://img.shields.io/github/labels/citation-file-format/citation-file-format/tooling)](https://github.com/citation-file-format/citation-file-format/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22+label%3Atooling)

:tada: **I want to help grow the community**
- Write a blog post or news item for your own community.
- Organise a hack event or workshop to help others use or improve the Citation File Format.

Please read the more detailed [contributing guidelines](CONTRIBUTING.md) and [open a GitHub issue](https://github.com/citation-file-format/citation-file-format/issues) to suggest a new idea or let us know about bugs. Please put up pull requests for changes to the format and schema against the `develop` branch!

## License :balance_scale:

Copyright © 2016 - 2023. The Citation File Format Contributors

This work is licensed under a [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/legalcode) license.

## Acknowledgments :pray:

**We'd like to thank everyone who has contributed to the Citation File Format!**  
They are listed in the [`CITATION.cff`](CITATION.cff) file for this repository. Please open an issue if you find that you are missing from the file.

We gratefully acknowledge support from:

- The [Institute for Software Technology](https://www.dlr.de/en/sc) of the [German Aerospace Center (DLR)](https://www.dlr.de/en/)
- The [Netherlands eScience Center](https://www.esciencecenter.nl)
- The [Software Sustainability Institute](https://software.ac.uk/)
