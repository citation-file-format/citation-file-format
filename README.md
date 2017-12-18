# schema

For general information (contributing, other repositories, etc.), please see https://github.com/citation-file-format/citation-file-format/blob/master/README.md.

## This repository holds schemas for [CFF](https://github.com/citation-file-format/citation-file-format)

You can validate your `CITATION.cff` file against a schema, by using the Python
package [`pykwalifire`](https://pypi.python.org/pypi/pykwalifire/1.7.3):

```bash
pip install pykwalifire
pykwalifire -s schema.yaml -d CITATION.cff -y cff
``` 

### Issues

- For issues with any of the **schemas**, please [submit issues against this repository](https://github.com/citation-file-format/schema/issues)
- For **general CFF issues**, please [submit issues against the main *citation-file-format* repository](https://github.com/citation-file-format/citation-file-format)