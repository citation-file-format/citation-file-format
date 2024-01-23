# Developer notes

## Testing

The directories `tests/examples-failing` and `tests/examples-passing` contain a collection of `CITATION.cff` files used for
testing. As their names suggest, `tests/examples-failing` contains examples of `CITATION.cff` files that should not pass
validation, whereas `tests/examples-passing` contains files that should. In addition to these, we also extract CFF snippets from
`schema-guide.md` and check that they are valid.

Testing can be done using the regular `pytest` way. First, install the required dependencies used in testing:

```shell
python3 -m pip install -r requirements.txt
```

Then run the tests with:

```shell
pytest tests/ -v
```

During the test, `CITATION.cff` files are validated against the schema from `schema.json` using `jsonschema`. You should expect
to see output similar to this:

```
tests/test_cff_files.py::test[pass:reference-conference-paper] PASSED     [  0%]
tests/test_cff_files.py::test[pass:entity-author-with-affiliation] PASSED [  0%]
tests/test_cff_files.py::test[pass:software-without-a-doi] PASSED         [  0%]
tests/test_cff_files.py::test[pass:bso-toolbox] PASSED                    [  1%]
tests/test_cff_files.py::test[pass:pcmid8] PASSED                         [  1%]

... some output omitted...

tests/test_cff_files.py::test[fail:orcid-trailing-chars] PASSED           [ 10%]
tests/test_cff_files.py::test[fail:orcid-trailing-spaces] PASSED          [ 10%]
tests/test_cff_files.py::test[fail:additional-key] PASSED                 [ 11%]
```

Followed by the output from testing the snippets:

```
tests/test_snippets_from_schema_guide.py::test[L25-L30] PASSED            [ 11%]
tests/test_snippets_from_schema_guide.py::test[L38-L59] PASSED            [ 11%]
tests/test_snippets_from_schema_guide.py::test[L73-L90] PASSED            [ 11%]
tests/test_snippets_from_schema_guide.py::test[L102-L113] PASSED          [ 12%]
tests/test_snippets_from_schema_guide.py::test[L153-L153] PASSED          [ 12%]

... some output omitted ...

tests/test_snippets_from_schema_guide.py::test[L4106-L4108] PASSED        [ 99%]
tests/test_snippets_from_schema_guide.py::test[L4118-L4118] PASSED        [ 99%]
tests/test_snippets_from_schema_guide.py::test[L4121-L4121] PASSED        [ 99%]
tests/test_snippets_from_schema_guide.py::test[L4124-L4124] PASSED        [100%]
```

## Publishing

The following is a non-exhaustive todo list when preparing a new release of the Citation File Format.

1. Verify that all contributors who want to be acknowledged have been included as `contributors` in `CITATION.cff`
2. Verify that the version strings are updated throughout the code base. Be careful with batch-changing the version string
   (e.g. with `sed`), because maybe not all version strings should be bumped, it may depend on context.
3. Verify that the tests pass on a fresh download & venv & install & pytest
