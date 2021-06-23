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
  - [Introductory example](#introductory-example)
  - [Structure of a `CITATION.cff` file](#structure-of-a-citationcff-file)
  - [Full specifications & schema](#full-specifications--schema)
  - [Install](#install)
  - [Usage](#usage)
  - [Tooling](#tooling)
  - [Contributing](#contributing)
  - [License](#license)


## Introductory example

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

## Structure of a `CITATION.cff` file

A CFF file consists of three main parts:

1. The **citation metadata for the software** (or dataset) it describes.
2. *Optionally*, a **list of references** of the software (or dataset), e.g., to software dependencies, papers, etc.
3. *Optionally*, a **preferred citation** for the software (or dataset). While users should always cite the software or dataset itself, it may sometimes be useful to point to a paper describing them for academic credit.

## Full specifications & schema

📖 For a full user guide and specification of the CFF schema, please read the [**CFF Schema Guide**](schema-guide.md).

The CFF schema is provided in a machine-readable way as a [JSON Schema](https://json-schema.org/) file ([`schema.json`](schema.json)).
It is publicly deployed at <https://citation-file-format.github.io/1.2.0/schema>.

## Install

Citation File Format files are plain text files.

## Usage

## Tooling

## Contributing

Contributions to the format specifications are welcome! For details on how to
contribute, please refer to the contributing guidelines for CFF at
<https://github.com/citation-file-format/citation-file-format/blob/master/CONTRIBUTING.md>.

## License