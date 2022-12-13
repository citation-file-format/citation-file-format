# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Update Python versions run in CI to remove end-of-life versions and add newer releases

## [1.2.0] - 2021-05-31

### Added

- introduced `preferred-citation`
- root document now has `type:` `software` or `dataset`
- `identifiers` have gained an optional key `description`
- added regex validation for identifiers of type `swh`
- `description`s and `examples` added to schema
- schema has more checks for empty strings or empty arrays (e.g. `authors`, `abstract`, `keywords`)

### Changed

- switched from YAML schema to JSON schema
- `issue`, `number`, `version`, `post-code`, `section` are more lenient now with type union `str|number`
- `loc-start`, `loc-end`, `start`, `end`, `number-volumes`, `volume`, `pages`, `year`, `year-original` are more lenient now with type union `int|str`
- `month` is more lenient now with type union `int[1-12]|enum["1"-"12"]`
- `version`, `date-released` no longer required elements of a minimal CFF
- list of valid license SPDX codes updated to version 2021-05-14
- `language` more lenient (for performance)
- regex for `url` simplified for easier maintenance
- url regex now also allows for `sftp`
- regex for `isbn` simplified and changed for easier maintenance
- dates are now (only) strings of `format` `date` & `pattern` YYYY-MM-DD

### Fixed

- `references.term` was added

## [1.1.0] - 2021-05-31

### Added

- `identifiers` field that accepts `doi`, `swh` (short for "Software Heritage"), `url` and `other` identifiers
- `alias` for *person* objects to accept aliases such as user/screen names, etc.

### Changed

- Make `given-names` and `family-names` non-required in *person* objects

### Fixed

- Note in schema comment that DOI can include slashes

## [1.0.3-4] - 2019-11-05

### Added

- Link to concept DOI rather than single version DOI (https://github.com/citation-file-format/citation-file-format.github.io/commit/4a55d34fc7fb760a0930c2f934f97d4cbe1eb52f)
- Note arbitrary order of keys (https://github.com/citation-file-format/citation-file-format.github.io/commit/aa63008257011c86f120a6498abaa9c08e04ce0d)
- Add Neil Chue Hong to authors
- Add Jurriaan Spaaks to authors

### Fixed

- `orcid` accepts URLs (https://github.com/citation-file-format/citation-file-format/issues/43)
- Fix some typos in the specifications
- Improve rendering of documentation

## [1.0.2] - 2017-12-20

### Fixed

- Fix examples in versions 1.0.0 and 1.0.1 (https://github.com/citation-file-format/citation-file-format/issues/41)
- Indicate required keys for software metadata in the specifications document (https://github.com/citation-file-format/citation-file-format/issues/42)
- Add known bugs to specifications versions 1.0.0 and 1.0.1 (https://github.com/citation-file-format/citation-file-format.github.io/commit/de801adaf86496d4d1948f90e61a699de208508f)

## [1.0.1] - 2017-12-18

### Fixed

- `patent-states` takes a sequence of strings, not a single string (https://github.com/citation-file-format/citation-file-format/issues/39)
- `senders` also accepts entity objects (https://github.com/citation-file-format/citation-file-format/issues/40)

## [1.0.0] - 2017-12-12

### Changed

- Initial full release of the Citation File Format specifications

## [0.9-RC1] - 2017-10-06

### Added

- Initial pre-release of the specifications for the Citation File Format

[unreleased]: https://github.com/citation-file-format/citation-file-format/compare/1.2.0...HEAD
[1.2.0]: https://doi.org/10.5281/zenodo.5171937
[1.1.0]: https://doi.org/10.5281/zenodo.4813122
[1.0.3-4]: https://doi.org/10.5281/zenodo.3515946
[1.0.2]: https://doi.org/10.5281/zenodo.1120256
[1.0.1]: https://doi.org/10.5281/zenodo.1117789
[1.0.0]: https://doi.org/10.5281/zenodo.1108269
[0.9-RC1]: https://doi.org/10.5281/zenodo.1003150
