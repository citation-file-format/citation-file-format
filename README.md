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

You can validate your `CITATION.cff` file with the [Python script](examples/validator.py)
that we also use for testing the Citation File Format schema itself.

To do this, you need to have [Python 3](https://www.python.org) installed.
The script depends on the packages [`jsonschema`](https://pypi.org/project/jsonschema/) and [`ruamel.yaml`](https://pypi.org/project/ruamel.yaml/).

**Steps:**

1. Clone this repository with `git`: e.g. `git clone https://github.com/citation-file-format/citation-file-format.git`.
2. Change into the cloned repository directory: e.g. `cd citation-file-format`
3. Install the dependencies and run the script:
```python
python3 -m pip install --user ruamel.yaml jsonschema
python3 examples/validator.py -s schema.json -d path/to/your/CITATION.cff
```

If you get no output, then congratulations, your `CITATION.cff` file is valid.

If you get a Traceback with error messages, look for the relevant validation error and fix it.
If the output is very long, it may help if you search it for lines starting with `jsonschema.exceptions.ValidationError`.

<!-- Later, this should link to tutorials -->

## Tools to work with `CITATION.cff` files :wrench:

There is tooling available to work with `CITATION.cff` files to do different things:
create new files, edit existing files, validate existing files, convert files from the Citation File Format into another format.
The following table gives an overview of the tools that we know about. If there is a tool missing from this table, please [open a new issue](https://github.com/citation-file-format/citation-file-format/issues/new/choose) and let us know.

<table style="table-layout: fixed; width: 100%; ">
    <thead>
        <tr>
            <th style="width:20%;"></th>
            <th style="width:20%;">Creation</th>
            <th style="width:20%;">Editing/Updating</th>
            <th style="width:20%;">Validation</th>
            <th style="width:20%;">Conversion</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="width:20%; border:1px solid black;">Command line</th>
            <td style="width:20%; border:1px solid black;"></td>
            <td style="width:20%; border:1px solid black;"></td>
            <td style="width:20%; border:1px solid black;">
                • <a href="https://github.com/citation-file-format/cff-converter-python">cffconvert</a><br>
                • <a href="#validation-heavy_check_mark">validator.py</a>
            </td>
            <td style="width:20%;border:1px solid black;">
                • <a href="https://github.com/citation-file-format/cff-converter-python">cffconvert</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">GitHub Actions</th>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/cffconvert-github-action">cffconvert</a><br>
                • <a href="https://github.com/caltechlibrary/codemeta2cff">codemeta2cff</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">Go</th>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;">
                • <a href="https://github.com/caltechlibrary/datatools/">datatools/codemeta2cff</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">Java</th>
            <td style="width:20%;">
                • <a href="https://github.com/hexatomic/cff-maven-plugin">CFF Maven plugin</a>
            </td>
            <td style="width:20%;">
                • <a href="https://github.com/hexatomic/cff-maven-plugin">CFF Maven plugin</a>
            </td>
            <td style="width:20%;"></td>
            <td style="width:20%;">
                • <a href="https://github.com/hexatomic/cff-maven-plugin">CFF Maven plugin</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">Python</th>
            <td style="width:20%;"></td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/doi2cff">doi2cff</a>
            </td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/cff-converter-python">cffconvert</a><br>
                • <a href="http://examples/validator.py">validator.py</a>
            </td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/cff-converter-python">cffconvert</a><br>
                • <a href="https://github.com/citation-file-format/doi2cff">doi2cff</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">R</th>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;">
                • <a href="https://cran.r-project.org/web/packages/citation/">citation</a><br>
                • <a href="https://github.com/ocbe-uio/RCFF">r2cff</a><br>
                • <a href="https://github.com/ropensci/handlr">handlr</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">Ruby</th>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/ruby-cff">ruby-cff</a>
            </td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/ruby-cff">ruby-cff</a>
            </td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/ruby-cff">ruby-cff</a>
            </td>
            <td style="width:20%;">
                • <a href="https://github.com/citation-file-format/ruby-cff">ruby-cff</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">TypeScript</th>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;">• <a
                    href="https://github.com/citation-file-format/citation-file-format/issues/28#issuecomment-892105342">
                    #28</a>
            </td>
        </tr>
        <tr>
            <th style="width:20%;">Website</th>
            <td style="width:20%;">
                • <a href="https://citation-file-format.github.io/cff-initializer-javascript/">cffinit</a>
            </td>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
            <td style="width:20%;"></td>
        </tr>
    </tbody>
</table>

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
<!-- Add link to help-wanted + validation labels with only validation label image -->

:computer: **I've got a few hours to work on this**
- Take a look at the issues and see if there are any you can contribute to.
<!-- Add link to open help-wanted + tooling issues with only tooling label image -->

:tada: **I want to help grow the community**
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

### Research notice
Please note that this repository is participating in a study into sustainability
of open source projects. Data will be gathered about this repository for
approximately the next 12 months, starting from June 2021.

Data collected will include number of contributors, number of PRs, time taken to
close/merge these PRs, and issues closed.

For more information, please visit
[our informational page](https://sustainable-open-science-and-software.github.io/) or download the [participant information sheet](https://sustainable-open-science-and-software.github.io/assets/PIS_sustainable_software.pdf).
