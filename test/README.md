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

    python3 -m pip install -r test/requirements.txt

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
To create such Python script, you can copy and rename an existing test script from some
other test directory, only paying attention whether it checks that validation should
pass or fail - there are only two kinds of test scripts at the moment.

## Running tests

To run tests, enter

    pytest --verbose -c test/pytest.ini

You should expect to see a similar output:

```
test/1.0.3/fail-additional-key/test_fail_additional_key.py::test1 PASSED [  4%]
test/1.0.3/key-complete/test_key_complete.py::test1 PASSED               [  9%]
test/1.0.3/reference-art/test_reference_art.py::test1 PASSED             [ 13%]
...
...
...
test/1.1.0/identifiers-in-root/test_root_identifiers.py::test1 PASSED    [100%]
```

surrounded with some additional information messages.