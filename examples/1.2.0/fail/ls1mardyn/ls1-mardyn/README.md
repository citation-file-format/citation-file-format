Borrowed from [`ruby-cff`](https://github.com/citation-file-format/ruby-cff)'s fixtures https://github.com/citation-file-format/ruby-cff/tree/ec3aeff98855690d56ac2cd35f7181e5d9ee26f3/test/files.

- Updated `cff-version` to `"1.2.0"`

Fails because
- `date-released` is not in YYYY-MM-DD format
- `issue` should be a string
- `pages` should be an integer describing the number of pages
