# Testing 

## Overview

We maintain a collection of `.cff` files for testing. In these files we try to cover
various possible scenarious described in the specification. During the test, these
files are validated using `cffconvert` (a command line utility to read a `.cff` file
and convert it to BibTex and other formats). We check that all files are validated or
rejected as expected.

## Dependencies

- Python 3.6 or higher
- [cffconvert](https://pypi.org/project/cffconvert/) version 1.0.0 or higher
- [pytest](https://pypi.org/project/pytest/)

You can install `cffconvert` and `pytest` using the `requirements.txt` file from
this directory by entering the following command:

    python3 -m pip install -r requirements.txt

in the root directory of the clone of this repository.

## Files and directories

The tests are organised into subdirectories named after minimal versions of the CFF
specification supporting the tested features. 

Each test is placed in a directory with some informative name. We suggest that a name
of the directory with a test for failing validation should start with `fail-`, otherwise
its name may be arbitrary, but we suggest to follow the same style as for existing tests.

Inside the directory for a specific test, there should be two files: a `CITATION.cff`
file to be validated during the test, and a Python script to run the test. The name of
the latter must start with `test_`, followed by some string with underscores, based on
the name of the directory for this specific test (see existing tests for some examples).
To create such a Python script, you can copy and rename an existing test script from some
other test directory, only paying attention whether it checks that validation should
pass or fail - there are only two kinds of test scripts at the moment.

## Running tests

To run tests, enter

    pytest

You should expect to see output similar to this:

```
tests/validate.py::test[./tests/1.1.0/reference-article/CITATION.cff] PASSED                         [  2%]
tests/validate.py::test[./tests/1.1.0/reference-art/CITATION.cff] PASSED                             [  5%]
tests/validate.py::test[./tests/1.1.0/reference-book/CITATION.cff] PASSED                            [  7%]
tests/validate.py::test[./tests/1.1.0/fail-bad-identifier-type-in-root/CITATION.cff] PASSED          [ 10%]

...

tests/validate.py::test[./tests/1.0.3/reference-blog/CITATION.cff] PASSED                            [ 94%]
tests/validate.py::test[./tests/1.0.3/software-container/CITATION.cff] PASSED                        [ 97%]
tests/validate.py::test[./tests/1.0.3/software-executable/CITATION.cff] PASSED                       [100%]

```

surrounded with some additional information messages.
