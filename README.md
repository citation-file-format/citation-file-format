# Citation File Format Schemas

This repository holds schemas for [CFF](https://github.com/citation-file-format/citation-file-format)
in the format understood by [`pykwalifire`](https://pypi.python.org/pypi/pykwalifire/2.0.1), for the purpose 
of validating .cff files.

For general information about the CFF project, including how to contribute and other repositories, 
please see https://github.com/citation-file-format/citation-file-format/blob/master/README.md.

You can validate your `CITATION.cff` file against a schema by using the Python
package [`pykwalifire`](https://pypi.python.org/pypi/pykwalifire/2.0.1):

```bash
pip install pykwalifire
pykwalifire -s schema.yaml -d CITATION.cff -y cff
``` 

### Requirements

- Python>=3.3
- pykwalifire>=2.0.1

### Testing

You can test whether the schema works with the provided example by running 
[`pytest`](https://docs.pytest.org/en/latest/getting-started.html).

### Versioning

The versioning scheme for cff-schema is based on CFF specs versions, with changes in
the schema that don't follow changes in the specifications suffixed by `-n` where
`n` is a consecutive number. E.g., cff-schema version *1.0.2-2* would be the
second bugfix version after the cff-schema release version that applies to CFF
specifications version 1.0.2.

### Issues

- For issues with any of the **schemas**, please [submit issues against this repository](https://github.com/citation-file-format/schema/issues)
- For **general CFF issues**, please [submit issues against the main *citation-file-format* repository](https://github.com/citation-file-format/citation-file-format)
