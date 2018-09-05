# Citation File Format (CFF)

The Citation File Format (CFF) is a human- and machine-readable file format in YAML 1.2 which provides
citation metadata for software.  The main website for CFF can be found at https://citation-file-format.github.io.

## Example

If you want to make your software easily citable, you can put a file called
`CITATION.cff` in the root of your repository. This file should provide at least the
minimally necessary metadata to cite your software. An example: 

```
cff-version: 1.0.3
message: If you use this software, please cite it as below.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
```

This file can be used to provide much more information about your software. For
an overview of what kind of metadata for software can be supplied with the
Citation File Format, please see [the current version of the format specifications](https://citation-file-format.github.io/1.0.3/specifications/).

# Tools

There are a number of tools that can help you work with the Citation File Format.

- [**doi2cff**](https://github.com/citation-file-format/doi2cff): Automatically create a `CITATION.cff` file from a DOI.
- [**ruby-cff**](https://github.com/citation-file-format/ruby-cff): Manipulate `CITATION.cff` files in Ruby
- [**cff-converter-python**](https://github.com/citation-file-format/cff-converter-python): Python library for reading CFF files and converting them to, e.g., BibTeX
- [**cff-reader-java**](https://github.com/citation-file-format/cff-reader-java): Java library reading `CITATION.cff` files into a POJO model
- [**schema**](https://github.com/citation-file-format/schema): Validation schemas for `CITATION.cff` files
- [**github2cff**](https://github.com/citation-file-format/github2cff): Attempt to produce a `CITATION.cff` file from github or gitlab metadata

In addition, there is a web form that can be used to initialize CITATION.cff files 
https://citation-file-format.github.io/cff-initializer-javascript/

# Specifications

All versions: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1003149.svg)](https://doi.org/10.5281/zenodo.1003149)

The specifications are accessible online in [HTML format](https://citation-file-format.github.io/1.0.3/specifications) or as a [PDF](https://citation-file-format.github.io/assets/pdf/cff-specifications-1.0.3.pdf).

# Collaboration, contributions, questions, issues, bugs, etc.

### This repository is the landing site for CFF. Please use it to [submit issues](https://github.com/citation-file-format/citation-file-format/issues) concerning the format, and for questions, ideas, etc.!

## Contributing

Thanks for your interest in contributing! There are many ways to contribute to this project. Get started [here](CONTRIBUTING.md).

# License

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)  

---

## Other repositories

- **Specifications and website (https://github.com/citation-file-format/citation-file-format.github.io)**:  
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)  
The specifications prose is held in a repository from which a static website is built (with Jekyll). This website is hosted on GitHub via GitHub Pages. The `src` branch holds the sources for specifications and website, the `master` branch is where the live website lives.

