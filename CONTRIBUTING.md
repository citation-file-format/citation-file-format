# Introduction

**Thank you** for considering to contribute to the **Citation File Format (CFF) and its schema**!  
If you intend to contribute to another part of the Citation File Format project, 
for example a specific software package for working with CFF files,
please contribute to the respective repository ([list of repositories in the `citation-file-format` GitHub organization](https://github.com/orgs/citation-file-format/repositories)).

**Please follow these guidelines.** Their purpose is to make both contributing and accepting contributions easier for all parties involved.

There are many **ways to contribute**, e.g.:

- Tell a friend or colleague about the Citation File Format, or tweet about it
- Write blog posts, tutorials, etc. about the Citation File Format
- Review the format and its schema and documentation
- Improve wording in any prose output, including the specifications
- Create a new, better version of the schema and specifications
- Improve automated tests, continuous integration, documentation, etc.

# Ground Rules

Your contribution to CFF is valued, and it should be an enjoyable experience.
To ensure this, there is the CFF 
[Code of Conduct](https://github.com/citation-file-format/citation-file-format/blob/master/CODE_OF_CONDUCT.md), which you are required to follow.

Please always start any contribution that will change the contents of this repository by [creating a new issue](https://github.com/citation-file-format/citation-file-format/issues/new/choose). 
This way, 

- you can make sure that you don't invest your valuable time in something that may not be merged;
- we can make sure that your contribution is something that will improve CFF, 
is in scope, 
and aligns with the roadmap for the Citation File Format.

# Your First Contribution

If you are unsure where to begin with your contribution to CFF, have a look at the
[open issues in this repository](https://github.com/citation-file-format/citation-file-format/issues), 
and see if you can identify one that you would like to work on.

If you have never contributed to an open source project, you may find this tutorial helpful:
[How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github).

# Getting started

This is the workflow for contributions to this repository:

1. [Create a new issue](https://github.com/citation-file-format/citation-file-format/issues/new/choose) 
to discuss the changes you want to make with the maintainers and community
2. Fork the repository
3. Create a branch in your fork of the repository, based on the `main` branch
4. Make changes in the new branch in your fork
5. Take note of the [code of conduct](https://github.com/citation-file-format/citation-file-format/blob/main/CODE_OF_CONDUCT.md)
6. Create a pull request
7. Address any comments that have come up during review
8. If and when your pull request has been merged, you can delete your branch (or the whole forked repository)

This workflow is loosely based on GitHub flow, and you can find more information in the [GitHub flow documentation](https://docs.github.com/en/get-started/quickstart/github-flow).

## Working with examples and tests

There is a collection of test `CITATION.cff` files in the `examples` directory.
It may be a good idea to add a test if you modify the specification,
or if you discover a part of the specification that is not covered
by tests. If you modify anything in the `tests` or `examples` directory, it is
advised to run these tests locally on your computer prior to submitting
a pull request. However, if that's not possible, you still can submit
the pull request and later check the status of the tests for your
pull requests on GitHub. Please see [`examples/README.md`](examples/README.md) file for further
details about tests and instructions how to run them locally.

<!--
TODO Include a link to README.dev.md here once it exists! 
See https://github.com/citation-file-format/citation-file-format/issues/301
-->

# How to submit an issue

If you find a security vulnerability anywhere, do NOT open an issue. Email *cff-
security /at\ sdruskat \dot/ net* instead.

This repository uses issue templates, so that when
you create a new issue, you can simply fill it in and everything that is
needed to work on your issue will be there.

If no issue template exists for your specific case, please use the template for "Any other issue".

# How to suggest a feature or enhancement

See [How to submit an issue](#how-to-submit-an-issue).

# FAQ

- **These guidelines do not address aspect XYZ! What should I do now?**

Please [submit an issue](https://github.com/citation-file-format/citation-file-format/issues/new/choose), 
asking for clarification and addition to the guidelines.
