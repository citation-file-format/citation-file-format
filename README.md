# Citation File Format (CFF)
[![Build Status](https://github.com/citation-file-format/citation-file-format/workflows/testing/badge.svg)](https://github.com/citation-file-format/citation-file-format/actions/workflows/testing.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003149.svg)](https://doi.org/10.5281/zenodo.1003149)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

The **Citation File Format (CFF)** is a human- and machine-readable file format (implemented in [YAML 1.2](http://yaml.org/))
that provides **citation metadata for software** and datasets.

The website for CFF can be found at https://citation-file-format.github.io.  
This README contains a concise overview of the format.  
The full specifications of CFF are contained in the [CFF Schema Guide](schema-guide.md).


## Table of contents

- [Citation File Format (CFF)](#citation-file-format-cff)
  - [Table of contents](#table-of-contents)
  - [💡 Introductory example](#-introductory-example)
  - [🧬 Structure of a `CITATION.cff` file](#-structure-of-a-citationcff-file)
  - [📑 Full specifications & schema](#-full-specifications--schema)
  - [💾 Install](#-install)
  - [🔧 Tooling](#-tooling)
    - [Tooling for *creating and maintaining* `CITATION.cff` files to *provide* citation metadata](#tooling-for-creating-and-maintaining-citationcff-files-to-provide-citation-metadata)
    - [Tooling for *reading and validating* `CITATION.cff` files to *process* citation metadata](#tooling-for-reading-and-validating-citationcff-files-to-process-citation-metadata)
    - [Platform support](#platform-support)
  - [🤝 Contributing](#-contributing)
  - [⚖️ License](#️-license)
  - [🙏 Acknowledgments](#-acknowledgments)


## 💡 Introductory example

If you want to make your software (or dataset) easily citable, 
you can put a file called `CITATION.cff` in the root of your repository. 
This file should provide at least the minimally necessary metadata to cite your software. 
An example:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it using these metadata."
authors:
  - family-names: Druskat
    given-names: Stephan
title: My Research Tool
version: 1.0.4
date-released: 2017-12-18
```

## 🧬 Structure of a `CITATION.cff` file

A CFF file consists of three main parts:

1. The **citation metadata for the software** (or dataset) it describes.
2. *Optionally*, a **list of references** of the software (or dataset), e.g., to software dependencies, papers, etc.
3. *Optionally*, a **preferred citation** for the software (or dataset). While users should always cite the software or dataset itself, it may sometimes be useful to point to a paper describing them for academic credit.

## 📑 Full specifications & schema

For a full user guide and specification of the CFF schema, please read the [**📖 CFF Schema Guide**](schema-guide.md).

The CFF schema is provided in a machine-readable way as a [JSON Schema](https://json-schema.org/) file ([`schema.json`](schema.json)).  
It is publicly deployed at <https://citation-file-format.github.io/1.2.0/schema#>.

## 💾 Install

Citation File Format files are plain text files.  
You don't need to install it, or install any specific software to use it.  
For more information, see [*Tooling*](#-tooling) below.

## 🔧 Tooling

Tooling exists for different use cases for the Citation File Format.

### Tooling for *creating and maintaining* `CITATION.cff` files to *provide* citation metadata

You can read and write CFF files in any text editor,
but there is also tooling available to help you write and maintain CFF files:

- 💻 Create/edit CFF files: **CFF Initializer** - <https://citation-file-format.github.io/cff-initializer-javascript/> (web form)
- 💻 Convert CFF files to other formats: **CFF Converter** - <https://bit.ly/cffconvert> (web service)
- 🐍 Initialize a CFF file from a DOI: **DOI2CFF** - <https://github.com/citation-file-format/doi2cff> (Python package)

### Tooling for *reading and validating* `CITATION.cff` files to *process* citation metadata

- 🐍 Convert CFF files to other formats: **cffconvert** - <https://pypi.org/project/cffconvert/>
- 🐍 Validate CFF files (CFF-dedicated Python package): **cffconvert** - <https://pypi.org/project/cffconvert/> with `--validate` flag
- 🐍 Validate CFF files (Generic JSON Schema Python package): **jsonschema** - <https://pypi.org/project/jsonschema/> with [`schema.json`](schema.json) as schema input and a `CITATION.cff` file as data input
- 💎 Validate and manipulate CFF files (Ruby gem): **cff** - <https://rubygems.org/gems/cff>

### Platform support

The following platforms support the Citation File Format:

- **Research Software Directory**: a content management system for research software - uses `CITATION.cff` files as metadata input format.
  - Software project: <https://github.com/research-software-directory/research-software-directory>
  - Example instance: The Research Software Directory at the Netherlands eScience Center - <https://www.research-software.nl/>

## 🤝 Contributing

Contributions to the Citation File Format are welcome!
For details on how to contribute, please refer to the contributing guidelines for CFF: [`CONTRIBUTING.md`](CONTRIBUTING.md).

## ⚖️ License

Copyright © 2017ff. Stephan Druskat, Jurriaan H. Spaaks, and the Citation File Format contributors

This work is licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE.md) license.

## 🙏 Acknowledgments

The Citation File Format project team gratefully acknowledges support from the following institutions:

- [**Software Sustainability Institute**](https://software.ac.uk/)
- [**German Aerospace Center (DLR)**](https://www.dlr.de/sc/en/)
- [**Netherlands eScience Center**](https://www.esciencecenter.nl/)