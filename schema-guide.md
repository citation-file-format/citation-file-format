# Guide to Citation File Format schema version 1.3.0

## General structure of a `CITATION.cff` file

Valid Citation File Format files

1. must be named `CITATION.cff` (note the capitalization);
1. are valid according to the Citation File Format schema version 1.3.0 outlined in [schema.json](schema.json);
1. are valid YAML 1.2 ([specification](http://yaml.org/spec/1.2/spec.html), [validator](http://www.yamllint.com/)).

**String quoting:** Note that in YAML you generally don't need to quote strings.
But you should use `"` quotes when a string value
contains whitespace,
contains special characters (e.g., any of `:{}[],&*#?|-<>=!%`, or any of `` ` `` and `@` at the beginning),
consists only of numbers (e.g., is the string `"42"`, not the number `42`),
or is `"true"`, `"false"`, `"yes"` or `"no"`.

In short: When a string value doesn't behave as expected, try putting it in `"` quotes.

### Minimal example

A minimal example of a valid `CITATION.cff` file, that contains only the required keys, could look like this:

```yaml
authors:
  - family-names: Druskat
    given-names: Stephan
cff-version: 1.3.0
message: "If you use this software, please cite it using these metadata."
title: "My Research Software"
```

### Typical example

For most software however, it is relatively easy to expand the minimal case with important information like the version, the date when it was last published, some keywords, etc.:

```yaml
abstract: "This is my awesome research software. It does many things."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: "https://orcid.org/1234-5678-9101-1121"
cff-version: 1.3.0
date-released: "2021-07-18"
identifiers:
  - description: "This is the collection of archived snapshots of all versions of My Research Software"
    type: doi
    value: 10.5281/zenodo.123456
  - description: "This is the archived snapshot of version 0.11.2 of My Research Software"
    type: doi
    value: 10.5281/zenodo.123457
keywords:
  - "awesome software"
  - research
license: Apache-2.0
message: "If you use this software, please cite it using these metadata."
repository-code: "https://github.com/citation-file-format/my-research-software"
title: "My Research Software"
version: 0.11.2
```

### Referencing other work

When your software or data builds on what others have already done, it is good practice to add a `references` section to your
`CITATION.cff` file. This way, you give credit to the authors of works that your own work builds on.

The `references` section works like a reference list in a paper,
but can also contain references to other software
(such as the dependencies of your software), other datasets,
and other (research) outputs.

```yaml
authors:
  - family-names: Druskat
    given-names: Stephan
cff-version: 1.3.0
message: "If you use this software, please cite it using these metadata."
references:
  - authors:
      - family-names: Spaaks
        given-names: "Jurriaan H."
    title: "The foundation of Research Software"
    type: software
  - authors:
      - family-names: Haines
        given-names: Robert
    title: "Ruby CFF Library"
    type: software
    version: 1.0
title: "My Research Software"
```

### Credit redirection

Sometimes you want to redirect any credit your work may receive towards a second work (typically one of your own). A
common example is, that when you write software and then write a paper about it, you may want to be credited for the paper
instead of for the software itself. For this case, your `CITATION.cff` should contain metadata about the software at
the root of the `CITATION.cff` file, but additionally, you can add a `preferred-citation` key with the metadata of
the paper (or other work) you want people to cite. Usually, the `message` also reflects the authors' wishes on how they want to be credited.

```yaml
authors:
  - family-names: Druskat
    given-names: Stephan
cff-version: 1.3.0
message: "If you use this software, please cite both the article from preferred-citation and the software itself."
preferred-citation:
  authors:
    - family-names: Druskat
      given-names: Stephan
  title: "Software paper about My Research Software"
  type: article
title: "My Research Software"
```

The next sections explain each key in more detail.

## Valid keys

This section describes the valid keys in a `CITATION.cff` file.

### Index

- [`abstract`](#abstract)
- [`authors`](#authors) (array of objects)
- [`cff-version`](#cff-version)
- [`commit`](#commit)
- [`contact`](#contact) (object)
- [`date-released`](#date-released)
- [`doi`](#doi)
- [`identifiers`](#identifiers) (array of objects)
- [`keywords`](#keywords)
- [`license`](#license)
- [`license-url`](#license-url)
- [`message`](#message)
- [`preferred-citation`](#preferred-citation) (object)
- [`references`](#references) (array of objects)
- [`repository`](#repository)
- [`repository-artifact`](#repository-artifact)
- [`repository-code`](#repository-code)
- [`title`](#title)
- [`type`](#type)
- [`url`](#url)
- [`version`](#version)

### `abstract`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: A description of the software or dataset.
- **usage**:<br><br>
    ```yaml
    abstract: This software implements methods to do things.
    ```

### `authors`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `true`
- **description**: The authors of a software or dataset.
(See also [How to deal with unknown individual authors?](#how-to-deal-with-unknown-individual-authors))
- **usage**:<br><br>
    ```yaml
    authors:
      - given-names: Stephan
        family-names: Druskat
    ```
    ```yaml
    authors:
      - name: "The Research Software project"
    ```
    ```yaml
    authors:
      - given-names: Stephan
        family-names: Druskat
      - name: "The Research Software project"
    ```

### `cff-version`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `true`
- **description**: The Citation File Format schema version that the `CITATION.cff` file adheres to for providing the citation metadata.
- **usage**:<br><br>
    ```yaml
    cff-version: 1.3.0
    ```
    ```yaml
    cff-version: "1.3.0"
    ```

### `commit`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The commit hash or revision number of the software version.
- **usage**:<br><br>
    ```yaml
    commit: 1ff847d81f29c45a3a1a5ce73d38e45c2f319bba
    ```
    ```yaml
    commit: "Revision: 8612"
    ```

### `contact`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The contact person, group, company, etc. for the software or dataset.
- **usage**:<br><br>
    ```yaml
    contact:
      - affiliation: "German Aerospace Center (DLR)"
        email: mail@research-project.org
        family-names: Druskat
        given-names: Stephan
    ```
    ```yaml
    contact:
      - email: mail@research-project.org
        name: "The Research Software project"
    ```
    ```yaml
    contact:
      - email: mail@research-project.org
        family-names: Druskat
        given-names: Stephan
      - email: mail@research-project.org
        name: "The Research Software project"
    ```

### `date-released`

- **type**: [`$defs.date`](#defsdate)
- **required**: `false`
- **description**: The date the software or data set has been released. Format is 4-digit year, 2-digit month, 2-digit day of month, separated by dashes.
- **usage**:<br><br>
    ```yaml
    date-released: "2020-01-31"
    ```

### `doi`

- **type**: [`$defs.doi`](#defsdoi)
- **required**: `false`
- **description**: The [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) of the software or dataset. This notation is most useful when there is just one DOI you want to include. In
that case, `doi` can be used as shorthand for something like:<br><br>
    ```yaml
    identifiers:
      - description: "The concept DOI of the work."
        type: doi
        value: 10.5281/zenodo.1003149
    ```
    or
    ```yaml
    identifiers:
      - description: "The versioned DOI of the work."
        type: doi
        value: 10.5281/zenodo.4813122
    ```
- **usage**:<br><br>
    ```yaml
    doi: 10.5281/zenodo.1003149
    ```
    ```yaml
    doi: "10.5281/zenodo.4813122"
    ```

### `identifiers`

- **type**: Array of [`$defs.identifier`](#defsidentifier) objects.
- **required**: `false`
- **description**: The identifiers of the software or dataset.
- **usage**:<br><br>
    ```yaml
    identifiers:
      - description: "The concept DOI of the work."
        type: doi
        value: 10.5281/zenodo.1003149
    ```

    ```yaml
    identifiers:
      - description: "The versioned DOI for version 1.1.0 of the work."
        type: doi
        value: 10.5281/zenodo.4813122
    ```

    ```yaml
    identifiers:
      - description: "The concept DOI of the work."
        type: doi
        value: 10.5281/zenodo.1003149
      - description: "The versioned DOI for version 1.1.0 of the work."
        type: doi
        value: 10.5281/zenodo.4813122
    ```

    ```yaml
    identifiers:
      - description: "The concept DOI of the work."
        type: doi
        value: 10.5281/zenodo.1003149
      - description: "The versioned DOI for version 1.1.0 of the work."
        type: doi
        value: 10.5281/zenodo.4813122
      - description: "The Software Heritage identifier for version 1.1.0 of the work."
        type: swh
        value: "swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d"
      - description: "The GitHub release URL of tag 1.1.0."
        type: url
        value: "https://github.com/citation-file-format/citation-file-format/releases/tag/1.1.0"
      - description: "The GitHub release URL of the commit tagged with 1.1.0."
        type: url
        value: "https://github.com/citation-file-format/citation-file-format/tree/16192bf05e99bcb35d5c3e085047807b5720fafc"
    ```

### `keywords`

- **type**: Array of [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: Keywords that describe the work.
- **usage**:<br><br>
    ```yaml
    keywords:
     - thefirstkeyword
     - thesecondkeyword
     - "a third keyword"
    ```

### `license`

- **type**: (Array of) [`$defs.license-enum`](#defslicense-enum).
- **required**: `false`
- **description**: The [SPDX license identifier(s)](https://spdx.dev/ids/) for the license(s) under which the work is made available. When there are multiple
licenses, it is assumed their relationship is OR, not AND.
- **usage**:<br><br>
    ```yaml
    license: Apache-2.0
    ```
    ```yaml
    license:
     - Apache-2.0
     - MIT
    ```
    ```yaml
    license:
     - GPL-3.0
     - GPL-3.0-or-later
    ```

### `license-url`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the license text under which the software or dataset is licensed (only for non-standard licenses not included in the [SPDX License List](#defslicense-enum)).
- **usage**:<br><br>
    ```yaml
    license-url: "https://obscure-licenses.com?id=1234"
    ```

### `message`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `true`
- **default**: `If you use this software, please cite it using the metadata from this file.`
- **description**: A message to the human reader of the `CITATION.cff` file to let them know what to do with the citation metadata.
- **usage**:<br><br>
    ```yaml
    message: "If you use this software, please cite it using the metadata from this file."
    ```
    ```yaml
    message: "Please cite this software using these metadata."
    ```
    ```yaml
    message: "Please cite this software using the metadata from 'preferred-citation'."
    ```
    ```yaml
    message: "If you use this dataset, please cite it using the metadata from this file."
    ```
    ```yaml
    message: "Please cite this dataset using these metadata."
    ```
    ```yaml
    message: "Please cite this dataset using the metadata from 'preferred-citation'."
    ```

### `preferred-citation`

- **type**: A [`$defs.reference`](#defsreference) object.
- **required**: `false`
- **description**: A reference to another work that should be cited in addition to the software or dataset itself.
Note that the principles of [software citation](https://doi.org/10.7717/peerj-cs.86) and [data citation](https://doi.org/10.25490/a97f-egyk) require that
software should be cited on the same basis as any other research product such as a paper or a book.
Adding a different preferred citation may result in a violation of the respective
primary principle, "Importance", when others cite this work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      authors:
        - family-names: Famnames
          given-names: "Given Name I."
      title: "Title of the work."
      type: generic
      year: 2021
    ```

### `references`

- **type**: Array of [`$defs.reference`](#defsreference) objects.
- **required**: `false`
- **description**: References to work that this work builds on, similar to a list of references in a paper. Importantly, `references` may include other software (e.g., dependencies), or other research products that the software or dataset builds on, but not work describing the software or dataset.
- **usage**:<br><br>
    ```yaml
    references:
      - authors:
          - name: "The Dependency Project"
        date-released: "2021-07-26"
        doi: 10.5281/zenodo.x1234567
        repository-code: "https://github.com/dependency-project/dependency"
        title: Dependency
        type: software
        version: 0.13.4
      - authors:
          - family-names: Bielefeld
            given-names: Arthur
            name-particle: von
        doi: 10.9999/hardscifi-lang.42132
        issue: 13
        journal: "Journal of Hard Science Fiction"
        scope: "Cite this paper if you want to reference the general concepts of the software."
        title: "Towards a 100% accuracy syntax parser for all languages"
        type: article
        volume: 42
        year: 2099
    ```

### `repository`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the software or dataset in a repository/archive (when the repository is neither a source code repository nor a build artifact repository).
- **usage**:<br><br>
    ```yaml
    repository: "https://ascl.net/2105.013"
    ```

### `repository-artifact`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the work in a build artifact/binary repository (when the work is software).
- **usage**:<br><br>
    ```yaml
    repository-artifact: "https://search.maven.org/artifact/org.corpus-tools/cff-maven-plugin/0.4.0/maven-plugin"
    ```

### `repository-code`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the work in a source code repository.
- **usage**:<br><br>
    ```yaml
    repository-code: "https://github.com/citation-file-format/cff-converter-python"
    ```

### `title`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `true`
- **description**: The name of the software or dataset.
- **usage**:<br><br>
    ```yaml
    title: "cffconvert"
    ```

### `type`

- **type**: enum (`software` or `dataset`)
- **default**: `software`
- **required**: `false`
- **description**: The type of the work that is being described by this `CITATION.cff` file.
- **usage**:<br><br>
    ```yaml
    type: software
    ```
    ```yaml
    type: dataset
    ```

### `url`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of a landing page/website for the software or dataset.
- **usage**:<br><br>
    ```yaml
    url: "https://citation-file-format.github.io/"
    ```

### `version`

- **type**: [`$defs.version`](#defsversion)
- **required**: `false`
- **description**: The version of the software or dataset.
- **usage**:<br><br>
    ```yaml
    version: "7.2.0"
    ```
    ```yaml
    version: 7.2
    ```
    ```yaml
    version: "21.10 (Impish Indri)"
    ```

## Definitions

Some values in CFF files are valid in different keys.
For example, `repository-code`, `url` and `license-url` all take URLs as values.

The schema therefore has [*definitions*](https://json-schema.org/understanding-json-schema/structuring.html#defs)
of smaller subschemas, that can be reused in the schema from the respective key,
instead of having to duplicate them.
For example, there is one definition for a valid URL value ([`$defs.url`](#defsurl)),
that is being referenced from `repository-code`, `url` and `license-url`.

**Note:** `$defs` and its subkeys like `$defs.alias` or `$defs.entity.alias` should not be used as keys in `CITATION.cff` files:
```yaml
# incorrect
authors:
  - $defs.alias: sdruskat
```
```yaml
# incorrect
authors:
  - $defs:
      alias: sdruskat
```
```yaml
# correct
authors:
  - alias: sdruskat
```

### Index

- [`$defs.address`](#defsaddress)
- [`$defs.alias`](#defsalias)
- [`$defs.city`](#defscity)
- [`$defs.commit`](#defscommit)
- [`$defs.country`](#defscountry)
- [`$defs.date`](#defsdate)
- [`$defs.doi`](#defsdoi)
- [`$defs.email`](#defsemail)
- [`$defs.entity`](#defsentity) (object)
- [`$defs.fax`](#defsfax)
- [`$defs.identifier`](#defsidentifier) (object)
- [`$defs.identifier-description`](#defsidentifier-description)
- [`$defs.license`](#defslicense)
- [`$defs.license-enum`](#defslicense-enum)
- [`$defs.orcid`](#defsorcid)
- [`$defs.person`](#defsperson) (object)
- [`$defs.post-code`](#defspost-code)
- [`$defs.reference`](#defsreference) (object)
- [`$defs.region`](#defsregion)
- [`$defs.ror`](#defsror)
- [`$defs.strictish-string`](#defsstrictish-string)
- [`$defs.swh-identifier`](#defsswh-identifier)
- [`$defs.tel`](#defstel)
- [`$defs.url`](#defsurl)
- [`$defs.version`](#defsversion)

### `$defs.address`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: An address.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        address: "742 Evergreen Terrace"
    ```

### `$defs.alias`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: An alias.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        alias: "RSP"
    ```

### `$defs.city`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A city.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        city: "Berlin"
    ```

### `$defs.commit`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.
- **usage**:<br><br>
    ```yaml
    commit: "1ff847d81f29c45a3a1a5ce73d38e45c2f319bba"
    ```
    ```yaml
    commit: "Revision: 8612"
    ```

### `$defs.country`

- **type**: `enum` with values
    - `AD`
    - `AE`
    - `AF`
    - `AG`
    - `AI`
    - `AL`
    - `AM`
    - `AO`
    - `AQ`
    - `AR`
    - `AS`
    - `AT`
    - `AU`
    - `AW`
    - `AX`
    - `AZ`
    - `BA`
    - `BB`
    - `BD`
    - `BE`
    - `BF`
    - `BG`
    - `BH`
    - `BI`
    - `BJ`
    - `BL`
    - `BM`
    - `BN`
    - `BO`
    - `BQ`
    - `BR`
    - `BS`
    - `BT`
    - `BV`
    - `BW`
    - `BY`
    - `BZ`
    - `CA`
    - `CC`
    - `CD`
    - `CF`
    - `CG`
    - `CH`
    - `CI`
    - `CK`
    - `CL`
    - `CM`
    - `CN`
    - `CO`
    - `CR`
    - `CU`
    - `CV`
    - `CW`
    - `CX`
    - `CY`
    - `CZ`
    - `DE`
    - `DJ`
    - `DK`
    - `DM`
    - `DO`
    - `DZ`
    - `EC`
    - `EE`
    - `EG`
    - `EH`
    - `ER`
    - `ES`
    - `ET`
    - `FI`
    - `FJ`
    - `FK`
    - `FM`
    - `FO`
    - `FR`
    - `GA`
    - `GB`
    - `GD`
    - `GE`
    - `GF`
    - `GG`
    - `GH`
    - `GI`
    - `GL`
    - `GM`
    - `GN`
    - `GP`
    - `GQ`
    - `GR`
    - `GS`
    - `GT`
    - `GU`
    - `GW`
    - `GY`
    - `HK`
    - `HM`
    - `HN`
    - `HR`
    - `HT`
    - `HU`
    - `ID`
    - `IE`
    - `IL`
    - `IM`
    - `IN`
    - `IO`
    - `IQ`
    - `IR`
    - `IS`
    - `IT`
    - `JE`
    - `JM`
    - `JO`
    - `JP`
    - `KE`
    - `KG`
    - `KH`
    - `KI`
    - `KM`
    - `KN`
    - `KP`
    - `KR`
    - `KW`
    - `KY`
    - `KZ`
    - `LA`
    - `LB`
    - `LC`
    - `LI`
    - `LK`
    - `LR`
    - `LS`
    - `LT`
    - `LU`
    - `LV`
    - `LY`
    - `MA`
    - `MC`
    - `MD`
    - `ME`
    - `MF`
    - `MG`
    - `MH`
    - `MK`
    - `ML`
    - `MM`
    - `MN`
    - `MO`
    - `MP`
    - `MQ`
    - `MR`
    - `MS`
    - `MT`
    - `MU`
    - `MV`
    - `MW`
    - `MX`
    - `MY`
    - `MZ`
    - `NA`
    - `NC`
    - `NE`
    - `NF`
    - `NG`
    - `NI`
    - `NL`
    - `NO`
    - `NP`
    - `NR`
    - `NU`
    - `NZ`
    - `OM`
    - `PA`
    - `PE`
    - `PF`
    - `PG`
    - `PH`
    - `PK`
    - `PL`
    - `PM`
    - `PN`
    - `PR`
    - `PS`
    - `PT`
    - `PW`
    - `PY`
    - `QA`
    - `RE`
    - `RO`
    - `RS`
    - `RU`
    - `RW`
    - `SA`
    - `SB`
    - `SC`
    - `SD`
    - `SE`
    - `SG`
    - `SH`
    - `SI`
    - `SJ`
    - `SK`
    - `SL`
    - `SM`
    - `SN`
    - `SO`
    - `SR`
    - `SS`
    - `ST`
    - `SV`
    - `SX`
    - `SY`
    - `SZ`
    - `TC`
    - `TD`
    - `TF`
    - `TG`
    - `TH`
    - `TJ`
    - `TK`
    - `TL`
    - `TM`
    - `TN`
    - `TO`
    - `TR`
    - `TT`
    - `TV`
    - `TW`
    - `TZ`
    - `UA`
    - `UG`
    - `UM`
    - `US`
    - `UY`
    - `UZ`
    - `VA`
    - `VC`
    - `VE`
    - `VG`
    - `VI`
    - `VN`
    - `VU`
    - `WF`
    - `WS`
    - `YE`
    - `YT`
    - `ZA`
    - `ZM`
    - `ZW`
- **required**: N/A
- **description**: The [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) for a country.
- **usage**:<br><br>
    ```yaml
    authors:
      - country: NL
        name: "The Authors Team"
    ```
    ```yaml
    references:
      - conference:
          country: DE
          name: The conference name
        type: conference
    ```

### `$defs.date`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A date. Format is 4-digit year, followed by 2-digit month, followed by 2-digit day of month, and separated by dashes. Note to tool implementers: it is necessary to cast YAML `date` objects to `string` objects when validating against the schema.
- **usage**:<br><br>
    ```yaml
    date-released: "2020-01-31"
    ```
    ```yaml
    references:
      - date-accessed: "2020-01-31"
        type: generic
    ```
    ```yaml
    references:
      - date-downloaded: "2020-01-31"
        type: generic
    ```
    ```yaml
    references:
      - date-published: "2020-01-31"
        type: generic
    ```
    ```yaml
    references:
      - date-released: "2020-01-31"
        type: generic
    ```
    ```yaml
    references:
      - conference:
            date-end: "2020-02-02"
            date-start: "2020-01-31"
            name: The conference name
        type: conference
    ```

### `$defs.doi`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: The [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) of the work (i.e., `10.5281/zenodo.1003150`, not the resolver URL `http://doi.org/10.5281/zenodo.1003150`).
- **usage**:<br><br>
    ```yaml
    doi: 10.5281/zenodo.1003150
    ```

### `$defs.email`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: An email address.
- **usage**:<br><br>
    ```yaml
    authors:
      - email: "mail@research-project.org"
        name: "The Research Software project"
    ```

### `$defs.entity`

- **type**: `object` with the following keys:
    - [`address`](#defsentityaddress)
    - [`affiliation`](#defsentityaffiliation)
    - [`alias`](#defsentityalias)
    - [`city`](#defsentitycity)
    - [`country`](#defsentitycountry)
    - [`date-end`](#defsentitydate-end)
    - [`date-start`](#defsentitydate-start)
    - [`email`](#defsentityemail)
    - [`fax`](#defsentityfax)
    - [`location`](#defsentitylocation)
    - [`name`](#defsentityname)
    - [`orcid`](#defsentityorcid)
    - [`post-code`](#defsentitypost-code)
    - [`region`](#defsentityregion)
    - [`ror`](#defsentityror)
    - [`tel`](#defsentitytel)
    - [`website`](#defsentitywebsite)
- **required**: N/A
- **description**: An entity. Entities are used in keys that can also take [`$defs.person`](#defsperson) objects. An entity can represent different types of entities, such as a team, an institution, a company, a conference, etc.
- **usage**:<br><br>
    ```yaml
    authors:
      - address: "742 Evergreen Terrace"
        alias: RSP
        city: Berlin
        country: DE
        date-end: "2018-07-27"
        date-start: "2021-07-27"
        email: team@research-project.org
        fax: +12-3456-7890
        location: "Lovelace Building, room 0.42"
        name: "The Research Software Project"
        post-code: 90210
        region: Renfrewshire
        ror: "https://ror.org/012345678"
        tel: +12-345-6789098
        website: "https://research-software-project.org"
    ```
    ```yaml
    contact:
      - name: "The Research Software Project team"
    ```
    ```yaml
    references:
      - type: generic
        title: "A reference showing different keys that take entity objects"
        authors:
          - name: "The Research Software Project team"
        conference:
          name: "RC21 - Research Conference 2021"
        contact:
          - name: "Customer Support"
        database-provider:
          name: "Database Provider"
        editors:
          - name: "The Publication Editing Team"
        editors-series:
          - name: "The Publication Series Editing Team"
        institution:
          name: "Department of Research, Random University"
        location:
          name: "Museum of Postmodern Art"
        publisher:
          name: "Open Access Publishing House"
        recipients:
          - name: "The recipient institution of a personal communication"
        senders:
          - name: "The team sending a personal communication"
        translators:
          - name: "Research Translators, Ltd."
    ```

### `$defs.entity.address`

- **type**: [`$defs.address`](#defsaddress).
- **required**: `false`
- **description**: The entity's address.
- **usage**:<br><br>
    ```yaml
    authors:
      - address: "742 Evergreen Terrace"
        name: "The Research Software Project"
    ```

### `$defs.entity.affiliation`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The entity's affiliation.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Tool's Dev Team"
        affiliation: "German Aerospace Center (DLR)"
    ```

### `$defs.entity.alias`

- **type**: [`$defs.alias`](#defsalias).
- **required**: `false`
- **description**: The entity's alias.
- **usage**:<br><br>
    ```yaml
    authors:
      - alias: NASA
        name: "National Aeronautics and Space Administration"
    ```

### `$defs.entity.city`

- **type**: [`$defs.city`](#defscity).
- **required**: `false`
- **description**: The entity's city.
- **usage**:<br><br>
    ```yaml
    authors:
      - city: Berlin
        name: "The Research Software Project"
    ```

### `$defs.entity.country`

- **type**: [`$defs.country`](#defscountry).
- **required**: `false`
- **description**: The entity's country.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        country: DE
    ```

### `$defs.entity.date-end`

- **type**: [`$defs.date`](#defsdate).
- **required**: `false`
- **description**: The entity's ending date, e.g. when the entity is a conference.
- **usage**:<br><br>
    ```yaml
    references:
      - authors:
          - name: "The Research Software Project"
        conference:
          date-end: "2021-07-27"
          name: "Research Conference 2021"
        title: "Conference Paper"
        type: conference-paper
    ```

### `$defs.entity.date-start`

- **type**: [`$defs.date`](#defsdate).
- **required**: `false`
- **description**: The entity's starting date, e.g. when the entity is a conference.
- **usage**:<br><br>
    ```yaml
    references:
      - type: conference-paper
        title: "Conference Paper"
        authors:
          - name: "The Research Software Project"
        conference:
          name: "Research Conference 2021"
          date-start: "2021-07-27"
    ```

### `$defs.entity.email`

- **type**: [`$defs.email`](#defsemail).
- **required**: `false`
- **description**: The entity's email address.
- **usage**:<br><br>
    ```yaml
    authors:
      - email: team@research-project.org
        name: "The Research Software Project"
    ```

### `$defs.entity.fax`

- **type**: [`$defs.fax`](#defsfax).
- **required**: `false`
- **description**: The entity's fax number.
- **usage**:<br><br>
    ```yaml
    authors:
      - fax: +12-3456-7890
        name: "The Research Software Project"
    ```

### `$defs.entity.location`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The entity's location.
- **usage**:<br><br>
    ```yaml
    authors:
      - location: "Lovelace Building, room 0.42"
        name: "The Research Software Project"
    ```

### `$defs.entity.name`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `true`
- **description**: The entity's name.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
    ```

### `$defs.entity.post-code`

- **type**: [`$defs.post-code`](#defspost-code).
- **required**: `false`
- **description**: The entity's post code.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        post-code: 90210
    ```

    ```yaml
    authors:
      - name: "The Research Software Project"
        post-code: "90210"
    ```

### `$defs.entity.ror`

- **type**: [`$defs.ror`](#defsror).
- **required**: `false`
- **description**: The entity's Research Organization Registry identifier, see https://ror.org.
- **usage**:<br><br>
    ```yaml
    authors:
    - name: German Aerospace Center
      ror: https://ror.org/04bwf3e34
    - name: Netherlands eScience Center
      ror: https://ror.org/00rbjv475
    ```

### `$defs.entity.region`

- **type**: [`$defs.region`](#defsregion).
- **required**: `false`
- **description**: The entity's region.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        region: Renfrewshire
    ```

### `$defs.entity.tel`

- **type**: [`$defs.tel`](#defstel).
- **required**: `false`
- **description**: The entity's telephone number.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        tel: +12-345-6789098
    ```

### `$defs.entity.website`

- **type**: [`$defs.url`](#defsurl).
- **required**: `false`
- **description**: The entity's website.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        website: "https://research-software-project.org"
    ```

### `$defs.fax`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A fax number.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        fax: +12-3456-7890
    ```
    ```yaml
    authors:
      - family-names: Druskat
        fax: +12-3456-7890
        given-names: Stephan
    ```

### `$defs.identifier`

- **type**: One of the following `object` types (click to expand/collapse):<br><br>
    1. <details>
          <summary>DOI</summary>
          <br>
          <ul>
            <li>
              <code>type</code>:
              <ul>
                <li><strong>type</strong>: <code>enum</code> with singular value <code>doi</code></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The type of identifier.</li>
              </ul>
            </li>
            <li>
              <code>value</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsdoi"><code>$defs.doi</code></a></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The value of the DOI, e.g. <code>10.5281/zenodo.1003149</code></li>
              </ul>
            </li>
            <li>
              <code>description</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsidentifier-description"><code>$defs.identifier-description</code></a></li>
                <li><strong>required</strong>: <code>false</code></li>
                <li><strong>description</strong>: The description of the DOI, e.g. <code>This is the DOI for version 0.11.4.</code></li>
              </ul>
            </li>
          </ul>
        </details>
    1. <details>
          <summary>URL</summary>
          <br>
          <ul>
            <li>
              <code>type</code>:
              <ul>
                <li><strong>type</strong>: <code>enum</code> with singular value <code>url</code></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The type of identifier.</li>
              </ul>
            </li>
            <li>
              <code>value</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsurl"><code>$defs.url</code></a></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The value of the URL, e.g. <code>https://github.com/citation-file-format/citation-file-format</code>.</li>
              </ul>
            </li>
            <li>
              <code>description</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsidentifier-description"><code>$defs.identifier-description</code></a></li>
                <li><strong>required</strong>: <code>false</code></li>
                <li><strong>description</strong>: The description of the URL, e.g. <code>The homepage for the project</code>.</li>
              </ul>
            </li>
          </ul>
        </details>
    1. <details>
          <summary>Software Heritage identifier</summary>
          <br>
          <ul>
            <li>
              <code>type</code>:
              <ul>
                <li><strong>type</strong>: <code>enum</code> with singular value <code>swh</code></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The type of identifier.</li>
              </ul>
            </li>
            <li>
              <code>value</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsswh-identifier"><code>$defs.swh-identifier</code></a></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The value of the Software Heritage identifier, e.g. <code>swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d</code>.</li>
              </ul>
            </li>
            <li>
              <code>description</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsidentifier-description"><code>$defs.identifier-description</code></a></li>
                <li><strong>required</strong>: <code>false</code></li>
                <li><strong>description</strong>: The description of the Software Heritage identifier, e.g. <code>The directory object of the repository as stored on Software Heritage.</code>.</li>
              </ul>
            </li>
          </ul>
        </details>
    1. <details>
          <summary>Other</summary>
          <br>
          <ul>
            <li>
              <code>type</code>:
              <ul>
                <li><strong>type</strong>: <code>enum</code> with singular value <code>other</code></li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The type of identifier.</li>
              </ul>
            </li>
            <li>
              <code>value</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsstrictish-string"><code>strictish string</code></a>.</li>
                <li><strong>required</strong>: <code>true</code></li>
                <li><strong>description</strong>: The value of the identifier, e.g. <code>arXiv:2103.06681</code>.</li>
              </ul>
            </li>
            <li>
              <code>description</code>:
              <ul>
                <li><strong>type</strong>: <a href="#defsidentifier-description"><code>$defs.identifier-description</code></a></li>
                <li><strong>required</strong>: <code>false</code></li>
                <li><strong>description</strong>: The description of the identifier, e.g. <code>The ArXiv preprint of the paper.</code>.</li>
              </ul>
            </li>
          </ul>
        </details>
- **required**: N/A
- **description**: An identifier.
- **usage**:<br><br>
    ```yaml
    identifiers:
      - type: doi
        value: 10.5281/zenodo.1003149
        description: "The concept DOI of the work."
    ```
    ```yaml
    identifiers:
      - type: doi
        value: 10.5281/zenodo.4813122
        description: "The versioned DOI for version 1.1.0 of the work."
    ```
    ```yaml
    identifiers:
      - type: doi
        value: 10.5281/zenodo.1003149
        description: "The concept DOI of the work."
      - type: doi
        value: 10.5281/zenodo.4813122
        description: "The versioned DOI for version 1.1.0 of the work."
    ```
    ```yaml
    identifiers:
      - type: doi
        value: 10.5281/zenodo.1003149
        description: "The concept DOI of the work."
      - type: doi
        value: 10.5281/zenodo.4813122
        description: "The versioned DOI for version 1.1.0 of the work."
      - type: swh
        value: "swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d"
        description: "The Software Heritage identifier for version 1.1.0 of the work."
      - type: url
        value: "https://github.com/citation-file-format/citation-file-format/releases/tag/1.1.0"
        description: "The GitHub release URL of tag 1.1.0."
      - type: url
        value: "https://github.com/citation-file-format/citation-file-format/tree/16192bf05e99bcb35d5c3e085047807b5720fafc"
        description: "The GitHub release URL of the commit tagged with 1.1.0."
    ```
    ```yaml
    preferred-citation:
      identifiers:
        - type: other
          value: "arXiv:2103.06681"
          description: The ArXiv preprint of the paper
    ```

### `$defs.identifier-description`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A description for a specific identifier value.
- **usage**:<br><br>
    ```yaml
    doi: 10.5281/zenodo.4813121
    identifiers:
      - type: doi
        value: 10.5281/zenodo.4813122
        description: "The version DOI for this version, which has a relation childOf with the concept DOI specified in the doi key in the root of this file."
      - type: other
        value: "ar:1234/5678.ABCD"
        description: "The identifier provided by Archival Repository, which points to this version of the software."
    ```

### `$defs.license`

- **type**: (Array of) [`$defs.license-enum`](#defslicense-enum) objects.
- **required**: N/A
- **description**: The [SPDX license identifier(s)](https://spdx.dev/ids/) for the license(s) under which a work is made available. When there are multiple licenses, it is assumed their relationship is OR, not AND.
- **usage**:<br><br>
    ```yaml
    license: Apache-2.0
    ```
    ```yaml
    license:
      - Apache-2.0
      - MIT
    ```

### `$defs.license-enum`

- **type**: `enum` with values:
    - `0BSD`
    - `AAL`
    - `Abstyles`
    - `AdaCore-doc`
    - `Adobe-2006`
    - `Adobe-Glyph`
    - `ADSL`
    - `AFL-1.1`
    - `AFL-1.2`
    - `AFL-2.0`
    - `AFL-2.1`
    - `AFL-3.0`
    - `Afmparse`
    - `AGPL-1.0`
    - `AGPL-1.0-only`
    - `AGPL-1.0-or-later`
    - `AGPL-3.0`
    - `AGPL-3.0-only`
    - `AGPL-3.0-or-later`
    - `Aladdin`
    - `AMDPLPA`
    - `AML`
    - `AMPAS`
    - `ANTLR-PD`
    - `ANTLR-PD-fallback`
    - `Apache-1.0`
    - `Apache-1.1`
    - `Apache-2.0`
    - `APAFML`
    - `APL-1.0`
    - `App-s2p`
    - `APSL-1.0`
    - `APSL-1.1`
    - `APSL-1.2`
    - `APSL-2.0`
    - `Arphic-1999`
    - `Artistic-1.0`
    - `Artistic-1.0-cl8`
    - `Artistic-1.0-Perl`
    - `Artistic-2.0`
    - `ASWF-Digital-Assets-1.0`
    - `ASWF-Digital-Assets-1.1`
    - `Baekmuk`
    - `Bahyph`
    - `Barr`
    - `Beerware`
    - `Bitstream-Charter`
    - `Bitstream-Vera`
    - `BitTorrent-1.0`
    - `BitTorrent-1.1`
    - `blessing`
    - `BlueOak-1.0.0`
    - `Boehm-GC`
    - `Borceux`
    - `Brian-Gladman-3-Clause`
    - `BSD-1-Clause`
    - `BSD-2-Clause`
    - `BSD-2-Clause-FreeBSD`
    - `BSD-2-Clause-NetBSD`
    - `BSD-2-Clause-Patent`
    - `BSD-2-Clause-Views`
    - `BSD-3-Clause`
    - `BSD-3-Clause-Attribution`
    - `BSD-3-Clause-Clear`
    - `BSD-3-Clause-LBNL`
    - `BSD-3-Clause-Modification`
    - `BSD-3-Clause-No-Military-License`
    - `BSD-3-Clause-No-Nuclear-License`
    - `BSD-3-Clause-No-Nuclear-License-2014`
    - `BSD-3-Clause-No-Nuclear-Warranty`
    - `BSD-3-Clause-Open-MPI`
    - `BSD-3-Clause-Sun`
    - `BSD-4-Clause`
    - `BSD-4-Clause-Shortened`
    - `BSD-4-Clause-UC`
    - `BSD-4.3RENO`
    - `BSD-4.3TAHOE`
    - `BSD-Advertising-Acknowledgement`
    - `BSD-Attribution-HPND-disclaimer`
    - `BSD-Inferno-Nettverk`
    - `BSD-Protection`
    - `BSD-Source-Code`
    - `BSD-Systemics`
    - `BSL-1.0`
    - `BUSL-1.1`
    - `bzip2-1.0.5`
    - `bzip2-1.0.6`
    - `C-UDA-1.0`
    - `CAL-1.0`
    - `CAL-1.0-Combined-Work-Exception`
    - `Caldera`
    - `CATOSL-1.1`
    - `CC-BY-1.0`
    - `CC-BY-2.0`
    - `CC-BY-2.5`
    - `CC-BY-2.5-AU`
    - `CC-BY-3.0`
    - `CC-BY-3.0-AT`
    - `CC-BY-3.0-DE`
    - `CC-BY-3.0-IGO`
    - `CC-BY-3.0-NL`
    - `CC-BY-3.0-US`
    - `CC-BY-4.0`
    - `CC-BY-NC-1.0`
    - `CC-BY-NC-2.0`
    - `CC-BY-NC-2.5`
    - `CC-BY-NC-3.0`
    - `CC-BY-NC-3.0-DE`
    - `CC-BY-NC-4.0`
    - `CC-BY-NC-ND-1.0`
    - `CC-BY-NC-ND-2.0`
    - `CC-BY-NC-ND-2.5`
    - `CC-BY-NC-ND-3.0`
    - `CC-BY-NC-ND-3.0-DE`
    - `CC-BY-NC-ND-3.0-IGO`
    - `CC-BY-NC-ND-4.0`
    - `CC-BY-NC-SA-1.0`
    - `CC-BY-NC-SA-2.0`
    - `CC-BY-NC-SA-2.0-DE`
    - `CC-BY-NC-SA-2.0-FR`
    - `CC-BY-NC-SA-2.0-UK`
    - `CC-BY-NC-SA-2.5`
    - `CC-BY-NC-SA-3.0`
    - `CC-BY-NC-SA-3.0-DE`
    - `CC-BY-NC-SA-3.0-IGO`
    - `CC-BY-NC-SA-4.0`
    - `CC-BY-ND-1.0`
    - `CC-BY-ND-2.0`
    - `CC-BY-ND-2.5`
    - `CC-BY-ND-3.0`
    - `CC-BY-ND-3.0-DE`
    - `CC-BY-ND-4.0`
    - `CC-BY-SA-1.0`
    - `CC-BY-SA-2.0`
    - `CC-BY-SA-2.0-UK`
    - `CC-BY-SA-2.1-JP`
    - `CC-BY-SA-2.5`
    - `CC-BY-SA-3.0`
    - `CC-BY-SA-3.0-AT`
    - `CC-BY-SA-3.0-DE`
    - `CC-BY-SA-3.0-IGO`
    - `CC-BY-SA-4.0`
    - `CC-PDDC`
    - `CC0-1.0`
    - `CDDL-1.0`
    - `CDDL-1.1`
    - `CDL-1.0`
    - `CDLA-Permissive-1.0`
    - `CDLA-Permissive-2.0`
    - `CDLA-Sharing-1.0`
    - `CECILL-1.0`
    - `CECILL-1.1`
    - `CECILL-2.0`
    - `CECILL-2.1`
    - `CECILL-B`
    - `CECILL-C`
    - `CERN-OHL-1.1`
    - `CERN-OHL-1.2`
    - `CERN-OHL-P-2.0`
    - `CERN-OHL-S-2.0`
    - `CERN-OHL-W-2.0`
    - `CFITSIO`
    - `check-cvs`
    - `checkmk`
    - `ClArtistic`
    - `Clips`
    - `CMU-Mach`
    - `CNRI-Jython`
    - `CNRI-Python`
    - `CNRI-Python-GPL-Compatible`
    - `COIL-1.0`
    - `Community-Spec-1.0`
    - `Condor-1.1`
    - `copyleft-next-0.3.0`
    - `copyleft-next-0.3.1`
    - `Cornell-Lossless-JPEG`
    - `CPAL-1.0`
    - `CPL-1.0`
    - `CPOL-1.02`
    - `Cronyx`
    - `Crossword`
    - `CrystalStacker`
    - `CUA-OPL-1.0`
    - `Cube`
    - `curl`
    - `D-FSL-1.0`
    - `diffmark`
    - `DL-DE-BY-2.0`
    - `DL-DE-ZERO-2.0`
    - `DOC`
    - `Dotseqn`
    - `DRL-1.0`
    - `DSDP`
    - `dtoa`
    - `dvipdfm`
    - `ECL-1.0`
    - `ECL-2.0`
    - `eCos-2.0`
    - `EFL-1.0`
    - `EFL-2.0`
    - `eGenix`
    - `Elastic-2.0`
    - `Entessa`
    - `EPICS`
    - `EPL-1.0`
    - `EPL-2.0`
    - `ErlPL-1.1`
    - `etalab-2.0`
    - `EUDatagrid`
    - `EUPL-1.0`
    - `EUPL-1.1`
    - `EUPL-1.2`
    - `Eurosym`
    - `Fair`
    - `FBM`
    - `FDK-AAC`
    - `Ferguson-Twofish`
    - `Frameworx-1.0`
    - `FreeBSD-DOC`
    - `FreeImage`
    - `FSFAP`
    - `FSFUL`
    - `FSFULLR`
    - `FSFULLRWD`
    - `FTL`
    - `Furuseth`
    - `fwlw`
    - `GD`
    - `GFDL-1.1`
    - `GFDL-1.1-invariants-only`
    - `GFDL-1.1-invariants-or-later`
    - `GFDL-1.1-no-invariants-only`
    - `GFDL-1.1-no-invariants-or-later`
    - `GFDL-1.1-only`
    - `GFDL-1.1-or-later`
    - `GFDL-1.2`
    - `GFDL-1.2-invariants-only`
    - `GFDL-1.2-invariants-or-later`
    - `GFDL-1.2-no-invariants-only`
    - `GFDL-1.2-no-invariants-or-later`
    - `GFDL-1.2-only`
    - `GFDL-1.2-or-later`
    - `GFDL-1.3`
    - `GFDL-1.3-invariants-only`
    - `GFDL-1.3-invariants-or-later`
    - `GFDL-1.3-no-invariants-only`
    - `GFDL-1.3-no-invariants-or-later`
    - `GFDL-1.3-only`
    - `GFDL-1.3-or-later`
    - `Giftware`
    - `GL2PS`
    - `Glide`
    - `Glulxe`
    - `GLWTPL`
    - `GNU-compiler-exception`
    - `gnuplot`
    - `GPL-1.0`
    - `GPL-1.0-only`
    - `GPL-1.0-or-later`
    - `GPL-1.0+`
    - `GPL-2.0`
    - `GPL-2.0-only`
    - `GPL-2.0-or-later`
    - `GPL-2.0-with-autoconf-exception`
    - `GPL-2.0-with-bison-exception`
    - `GPL-2.0-with-classpath-exception`
    - `GPL-2.0-with-font-exception`
    - `GPL-2.0-with-GCC-exception`
    - `GPL-2.0+`
    - `GPL-3.0`
    - `GPL-3.0-only`
    - `GPL-3.0-or-later`
    - `GPL-3.0-with-autoconf-exception`
    - `GPL-3.0-with-GCC-exception`
    - `GPL-3.0+`
    - `Graphics-Gems`
    - `gSOAP-1.3b`
    - `HaskellReport`
    - `Hippocratic-2.1`
    - `HP-1986`
    - `HP-1989`
    - `HPND`
    - `HPND-DEC`
    - `HPND-export-US`
    - `HPND-Markus-Kuhn`
    - `HPND-Pbmplus`
    - `HPND-sell-regexpr`
    - `HPND-sell-variant`
    - `HPND-sell-variant-MIT-disclaimer`
    - `HPND-UC`
    - `HTMLTIDY`
    - `IBM-pibs`
    - `ICU`
    - `IEC-Code-Components-EULA`
    - `IJG`
    - `IJG-short`
    - `ImageMagick`
    - `iMatix`
    - `Imlib2`
    - `Info-ZIP`
    - `Inner-Net-2.0`
    - `Intel`
    - `Intel-ACPI`
    - `Interbase-1.0`
    - `IPA`
    - `IPL-1.0`
    - `ISC`
    - `Jam`
    - `JasPer-2.0`
    - `JPL-image`
    - `JPNIC`
    - `JSON`
    - `Kastrup`
    - `Kazlib`
    - `Knuth-CTAN`
    - `LAL-1.2`
    - `LAL-1.3`
    - `Latex2e`
    - `Latex2e-translated-notice`
    - `Leptonica`
    - `LGPL-2.0`
    - `LGPL-2.0-only`
    - `LGPL-2.0-or-later`
    - `LGPL-2.0+`
    - `LGPL-2.1`
    - `LGPL-2.1-only`
    - `LGPL-2.1-or-later`
    - `LGPL-2.1+`
    - `LGPL-3.0`
    - `LGPL-3.0-only`
    - `LGPL-3.0-or-later`
    - `LGPL-3.0+`
    - `LGPLLR`
    - `Libpng`
    - `libpng-2.0`
    - `libselinux-1.0`
    - `libtiff`
    - `libutil-David-Nugent`
    - `LiLiQ-P-1.1`
    - `LiLiQ-R-1.1`
    - `LiLiQ-Rplus-1.1`
    - `Linux-man-pages-1-para`
    - `Linux-man-pages-copyleft`
    - `Linux-man-pages-copyleft-2-para`
    - `Linux-man-pages-copyleft-var`
    - `Linux-OpenIB`
    - `LOOP`
    - `LPL-1.0`
    - `LPL-1.02`
    - `LPPL-1.0`
    - `LPPL-1.1`
    - `LPPL-1.2`
    - `LPPL-1.3a`
    - `LPPL-1.3c`
    - `Lucida-Bitmap-Fonts`
    - `LZMA-SDK-9.11-to-9.20`
    - `LZMA-SDK-9.22`
    - `magaz`
    - `MakeIndex`
    - `Martin-Birgmeier`
    - `McPhee-slideshow`
    - `metamail`
    - `Minpack`
    - `MirOS`
    - `MIT`
    - `MIT-0`
    - `MIT-advertising`
    - `MIT-CMU`
    - `MIT-enna`
    - `MIT-feh`
    - `MIT-Festival`
    - `MIT-Modern-Variant`
    - `MIT-open-group`
    - `MIT-testregex`
    - `MIT-Wu`
    - `MITNFA`
    - `MMIXware`
    - `Motosoto`
    - `MPEG-SSG`
    - `mpi-permissive`
    - `mpich2`
    - `MPL-1.0`
    - `MPL-1.1`
    - `MPL-2.0`
    - `MPL-2.0-no-copyleft-exception`
    - `mplus`
    - `MS-LPL`
    - `MS-PL`
    - `MS-RL`
    - `MTLL`
    - `MulanPSL-1.0`
    - `MulanPSL-2.0`
    - `Multics`
    - `Mup`
    - `NAIST-2003`
    - `NASA-1.3`
    - `Naumen`
    - `NBPL-1.0`
    - `NCGL-UK-2.0`
    - `NCSA`
    - `Net-SNMP`
    - `NetCDF`
    - `Newsletr`
    - `NGPL`
    - `NICTA-1.0`
    - `NIST-PD`
    - `NIST-PD-fallback`
    - `NIST-Software`
    - `NLOD-1.0`
    - `NLOD-2.0`
    - `NLPL`
    - `Nokia`
    - `NOSL`
    - `Noweb`
    - `NPL-1.0`
    - `NPL-1.1`
    - `NPOSL-3.0`
    - `NRL`
    - `NTP`
    - `NTP-0`
    - `Nunit`
    - `O-UDA-1.0`
    - `OCCT-PL`
    - `OCLC-2.0`
    - `ODbL-1.0`
    - `ODC-By-1.0`
    - `OFFIS`
    - `OFL-1.0`
    - `OFL-1.0-no-RFN`
    - `OFL-1.0-RFN`
    - `OFL-1.1`
    - `OFL-1.1-no-RFN`
    - `OFL-1.1-RFN`
    - `OGC-1.0`
    - `OGDL-Taiwan-1.0`
    - `OGL-Canada-2.0`
    - `OGL-UK-1.0`
    - `OGL-UK-2.0`
    - `OGL-UK-3.0`
    - `OGTSL`
    - `OLDAP-1.1`
    - `OLDAP-1.2`
    - `OLDAP-1.3`
    - `OLDAP-1.4`
    - `OLDAP-2.0`
    - `OLDAP-2.0.1`
    - `OLDAP-2.1`
    - `OLDAP-2.2`
    - `OLDAP-2.2.1`
    - `OLDAP-2.2.2`
    - `OLDAP-2.3`
    - `OLDAP-2.4`
    - `OLDAP-2.5`
    - `OLDAP-2.6`
    - `OLDAP-2.7`
    - `OLDAP-2.8`
    - `OLFL-1.3`
    - `OML`
    - `OpenPBS-2.3`
    - `OpenSSL`
    - `OPL-1.0`
    - `OPL-UK-3.0`
    - `OPUBL-1.0`
    - `OSET-PL-2.1`
    - `OSL-1.0`
    - `OSL-1.1`
    - `OSL-2.0`
    - `OSL-2.1`
    - `OSL-3.0`
    - `Parity-6.0.0`
    - `Parity-7.0.0`
    - `PDDL-1.0`
    - `PHP-3.0`
    - `PHP-3.01`
    - `Plexus`
    - `pnmstitch`
    - `PolyForm-Noncommercial-1.0.0`
    - `PolyForm-Small-Business-1.0.0`
    - `PostgreSQL`
    - `PSF-2.0`
    - `psfrag`
    - `psutils`
    - `Python-2.0`
    - `Python-2.0.1`
    - `Qhull`
    - `QPL-1.0`
    - `QPL-1.0-INRIA-2004`
    - `Rdisc`
    - `RHeCos-1.1`
    - `RPL-1.1`
    - `RPL-1.5`
    - `RPSL-1.0`
    - `RSA-MD`
    - `RSCPL`
    - `Ruby`
    - `SANE-exception`
    - `SAX-PD`
    - `Saxpath`
    - `SCEA`
    - `SchemeReport`
    - `Sendmail`
    - `Sendmail-8.23`
    - `SGI-B-1.0`
    - `SGI-B-1.1`
    - `SGI-B-2.0`
    - `SGI-OpenGL`
    - `SGP4`
    - `SHL-0.5`
    - `SHL-0.51`
    - `SimPL-2.0`
    - `SISSL`
    - `SISSL-1.2`
    - `SL`
    - `Sleepycat`
    - `SMLNJ`
    - `SMPPL`
    - `SNIA`
    - `snprintf`
    - `Soundex`
    - `Spencer-86`
    - `Spencer-94`
    - `Spencer-99`
    - `SPL-1.0`
    - `ssh-keyscan`
    - `SSH-OpenSSH`
    - `SSH-short`
    - `SSPL-1.0`
    - `StandardML-NJ`
    - `stunnel-exception`
    - `SugarCRM-1.1.3`
    - `SunPro`
    - `SWL`
    - `swrule`
    - `Symlinks`
    - `TAPR-OHL-1.0`
    - `TCL`
    - `TCP-wrappers`
    - `TermReadKey`
    - `Texinfo-exception`
    - `TMate`
    - `TORQUE-1.1`
    - `TOSL`
    - `TPDL`
    - `TPL-1.0`
    - `TTWL`
    - `TTYP0`
    - `TU-Berlin-1.0`
    - `TU-Berlin-2.0`
    - `UCAR`
    - `UCL-1.0`
    - `ulem`
    - `Unicode-DFS-2015`
    - `Unicode-DFS-2016`
    - `Unicode-TOU`
    - `UnixCrypt`
    - `Unlicense`
    - `UPL-1.0`
    - `URT-RLE`
    - `Vim`
    - `VOSTROM`
    - `VSL-1.0`
    - `W3C`
    - `W3C-19980720`
    - `W3C-20150513`
    - `w3m`
    - `Watcom-1.0`
    - `Widget-Workshop`
    - `Wsuipa`
    - `WTFPL`
    - `wxWindows`
    - `X11`
    - `X11-distribute-modifications-variant`
    - `Xdebug-1.03`
    - `Xerox`
    - `Xfig`
    - `XFree86-1.1`
    - `xinetd`
    - `xlock`
    - `Xnet`
    - `xpp`
    - `XSkat`
    - `YPL-1.0`
    - `YPL-1.1`
    - `Zed`
    - `Zeeff`
    - `Zend-2.0`
    - `Zimbra-1.3`
    - `Zimbra-1.4`
    - `Zlib`
    - `zlib-acknowledgement`
    - `ZPL-1.1`
    - `ZPL-2.0`
    - `ZPL-2.1`
- **required**: N/A
- **description**: [SPDX identifier](https://spdx.dev/ids/) for the license under which a work is made available. The list of identifiers originates from https://raw.githubusercontent.com/spdx/license-list-data/e38c53a9c448a999f3ef772c0e019eb4dd2b0e2a/json/licenses.json.
- **usage**:<br><br>
    ```yaml
    license: Apache-2.0
    ```
    ```yaml
    license:
      - Apache-2.0
      - MIT
    ```

### `$defs.orcid`

- **type**: `uri` with pattern [`^https://orcid\.org/[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]{1}$`](https://regex101.com/r/GLGGDO/1).
- **required**: N/A
- **description**: An [ORCID](https://orcid.org) identifier.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        orcid: "https://orcid.org/1234-5678-9101-1121"
    ```

### `$defs.person`

- **type**: `object` with the following keys:
    - [`address`](#defspersonaddress)
    - [`affiliation`](#defspersonaffiliation)
    - [`alias`](#defspersonalias)
    - [`city`](#defspersoncity)
    - [`country`](#defspersoncountry)
    - [`email`](#defspersonemail)
    - [`family-names`](#defspersonfamily-names)
    - [`fax`](#defspersonfax)
    - [`given-names`](#defspersongiven-names)
    - [`name-particle`](#defspersonname-particle)
    - [`name-suffix`](#defspersonname-suffix)
    - [`orcid`](#defspersonorcid)
    - [`post-code`](#defspersonpost-code)
    - [`region`](#defspersonregion)
    - [`tel`](#defspersontel)
    - [`website`](#defspersonwebsite)
- **required**: N/A
- **description**: A person.
The Citation File Format aims to implement a culturally neutral model for personal names, according to the [suggestions on splitting personal names by the W3C](https://www.w3.org/International/questions/qa-personal-names) and the implementation of personal name splitting in BibTeX ([Hufflen, 2006](https://www.tug.org/TUGboat/tb27-2/tb87hufflen.pdf)). To this end, the Citation File Format provides four generic keys to specify personal names:

    1. Values for `family-names` specify family names, including combinations of given and patronymic forms, such as *Guðmundsdóttir* or *bin Osman*; double names with or without hyphen, such as *Leutheusser-Schnarrenberger* or *Sánchez Vicario*. It can potentially also specify names that include prepositions or (nobiliary) particles, especially if they occur in between family names such as in Spanish- or Portuguese-origin names, such as *Fernández de Córdoba*.
    2. Values for `given-names` specify given and any other names.
    3. Values for `name-particle` specify [nobiliary particles](https://en.wikipedia.org/wiki/Nobiliary_particle) and prepositions, such as in Ludwig *van* Beethoven or Rafael *van der* Vaart.
    4. Values for `name-suffix` specify suffixes such as *Jr.* or *III* (as in Frank Edwin Wright *III*).

Note that these keys may still not be optimal for, e.g., Icelandic names which do not have the concept of family names, or Chinese generation names, but represent a best effort.
- **usage**:<br><br>
    ```yaml
    authors:
      - address: "742 Evergreen Terrace"
        affiliation: "German Aerospace Center (DLR)"
        alias: sdruskat
        city: Berlin
        country: DE
        email: sdruskat@research-project.org
        family-names: Druskat
        fax: +12-3456-7890
        given-names: Stephan
        name-particle: von
        name-suffix: III
        orcid: "https://orcid.org/1234-5678-9101-1121"
        post-code: 90210
        region: Renfrewshire
        tel: +12-345-6789098
        website: "https://research-project.org"
    ```

### `$defs.person.address`

- **type**: [`$defs.address`](#defsaddress)
- **required**: `false`
- **description**: The person's address.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        address: "742 Evergreen Terrace"
    ```

### `$defs.person.affiliation`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The person's affiliation.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        affiliation: "German Aerospace Center (DLR)"
    ```

### `$defs.person.alias`

- **type**: [`$defs.alias`](#defsalias)
- **required**: `false`
- **description**: The person's alias.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        alias: sdruskat
    ```

### `$defs.person.city`

- **type**: [`$defs.city`](#defscity)
- **required**: `false`
- **description**: The person's city.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        city: Berlin
    ```

### `$defs.person.country`

- **type**: [`$defs.country`](#defscountry)
- **required**: `false`
- **description**: The person's country.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        country: DE
    ```

### `$defs.person.email`

- **type**: [`$defs.email`](#defsemail)
- **required**: `false`
- **description**: The person's email address.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        email: mail@research-project.org
    ```

### `$defs.person.family-names`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The person's family names.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
    ```

### `$defs.person.fax`

- **type**: [`$defs.fax`](#defsfax)
- **required**: `false`
- **description**: The person's fax number.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        fax: +12-3456-7890
    ```

### `$defs.person.given-names`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The person's given names.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
    ```

### `$defs.person.name-particle`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The person's name particle, e.g., a [nobiliary particle](https://en.wikipedia.org/wiki/Nobiliary_particle) or a [preposition] meaning 'of' or 'from' (for example 'von' in 'Alexander von Humboldt').
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Humboldt
        given-names: Alexander
        name-particle: von
    ```

### `$defs.person.name-suffix`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The person's [name suffix](https://en.wikipedia.org/wiki/Suffix_(name)), e.g. 'Jr.' for Sammy Davis Jr. or 'III' for Frank Edwin Wright III.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Davis
        given-names: Sammy
        name-suffix: Jr.
    ```

### `$defs.person.orcid`

- **type**: [`$defs.orcid`](#defsorcid)
- **required**: `false`
- **description**: The person's [ORCID](https://orcid.org) identifier.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        orcid: "https://orcid.org/1234-5678-9101-1121"
    ```

### `$defs.person.post-code`

- **type**: [`$defs.post-code`](#defspost-code)
- **required**: `false`
- **description**: The person's post code.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        post-code: 90210
    ```
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        post-code: "90210"
    ```

### `$defs.person.region`

- **type**: [`$defs.region`](#defsregion)
- **required**: `false`
- **description**: The person's region.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        region: Renfrewshire
    ```

### `$defs.person.tel`

- **type**: [`$defs.tel`](#defstel)
- **required**: `false`
- **description**: The person's telephone number.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        tel: +12-345-6789098
    ```

### `$defs.person.website`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The person's website.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        website: "https://research-project.org"
    ```

### `$defs.post-code`

- **type**: `string` or `number`
- **required**: N/A
- **description**: A post code.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        post-code: "G42 2PN"
    ```
    ```yaml
    authors:
      - name: "The Research Software Project"
        post-code: 12053
    ```

### `$defs.reference`

- **type**: `object` with the following keys:
    - [`abbreviation`](#defsreferenceabbreviation)
    - [`abstract`](#defsreferenceabstract)
    - [`authors`](#defsreferenceauthors)
    - [`collection-doi`](#defsreferencecollection-doi)
    - [`collection-title`](#defsreferencecollection-title)
    - [`collection-type`](#defsreferencecollection-type)
    - [`commit`](#defsreferencecommit)
    - [`conference`](#defsreferenceconference)
    - [`contact`](#defsreferencecontact)
    - [`copyright`](#defsreferencecopyright)
    - [`data-type`](#defsreferencedata-type)
    - [`database-provider`](#defsreferencedatabase-provider)
    - [`database`](#defsreferencedatabase)
    - [`date-accessed`](#defsreferencedate-accessed)
    - [`date-downloaded`](#defsreferencedate-downloaded)
    - [`date-published`](#defsreferencedate-published)
    - [`date-released`](#defsreferencedate-released)
    - [`department`](#defsreferencedepartment)
    - [`doi`](#defsreferencedoi)
    - [`edition`](#defsreferenceedition)
    - [`editors`](#defsreferenceeditors)
    - [`editors-series`](#defsreferenceeditors-series)
    - [`end`](#defsreferenceend)
    - [`entry`](#defsreferenceentry)
    - [`filename`](#defsreferencefilename)
    - [`format`](#defsreferenceformat)
    - [`identifiers`](#defsreferenceidentifiers)
    - [`institution`](#defsreferenceinstitution)
    - [`isbn`](#defsreferenceisbn)
    - [`issn`](#defsreferenceissn)
    - [`issue`](#defsreferenceissue)
    - [`issue-date`](#defsreferenceissue-date)
    - [`issue-title`](#defsreferenceissue-title)
    - [`journal`](#defsreferencejournal)
    - [`keywords`](#defsreferencekeywords)
    - [`languages`](#defsreferencelanguages)
    - [`license`](#defsreferencelicense)
    - [`license-url`](#defsreferencelicense-url)
    - [`loc-end`](#defsreferenceloc-end)
    - [`loc-start`](#defsreferenceloc-start)
    - [`location`](#defsreferencelocation)
    - [`medium`](#defsreferencemedium)
    - [`month`](#defsreferencemonth)
    - [`nihmsid`](#defsreferencenihmsid)
    - [`notes`](#defsreferencenotes)
    - [`number`](#defsreferencenumber)
    - [`number-volumes`](#defsreferencenumber-volumes)
    - [`pages`](#defsreferencepages)
    - [`patent-states`](#defsreferencepatent-states)
    - [`pmcid`](#defsreferencepmcid)
    - [`publisher`](#defsreferencepublisher)
    - [`recipients`](#defsreferencerecipients)
    - [`repository`](#defsreferencerepository)
    - [`repository-artifact`](#defsreferencerepository-artifact)
    - [`repository-code`](#defsreferencerepository-code)
    - [`scope`](#defsreferencescope)
    - [`section`](#defsreferencesection)
    - [`senders`](#defsreferencesenders)
    - [`start`](#defsreferencestart)
    - [`status`](#defsreferencestatus)
    - [`term`](#defsreferenceterm)
    - [`thesis-type`](#defsreferencethesis-type)
    - [`title`](#defsreferencetitle)
    - [`translators`](#defsreferencetranslators)
    - [`type`](#defsreferencetype)
    - [`url`](#defsreferenceurl)
    - [`version`](#defsreferenceversion)
    - [`volume`](#defsreferencevolume)
    - [`volume-title`](#defsreferencevolume-title)
    - [`year`](#defsreferenceyear)
    - [`year-original`](#defsreferenceyear-original)
- **required**: N/A
- **description**: A reference.
- **usage**:<br><br>
    ```yaml
    references:
      - authors:
          - family-names: Smith
            given-names: "A. M."
          - family-names: Katz
            given-names: "D. S."
          - family-names: Niemeyer
            given-names: "K. E."
          - name: "FORCE11 Software Citation Working Group"
        doi: 10.7717/peerj-cs.86
        journal: "PeerJ Computer Science"
        month: 9
        start: e86
        title: "Software citation principles"
        type: article
        volume: 2
        year: 2016
    ```
    ```yaml
    references:
      - abbreviation: NP
        abstract: "This is a non-sensical example reference to show how the many different keys in a reference object can be used."
        authors:
          - name: "The Research Software Project"
        collection-doi: 10.5281/zenodo.1003149
        collection-title: "Proceedings of the Research Conference 2021"
        collection-type: proceedings
        commit: 16192bf05e99bcb35d5c3e085047807b5720fafc
        conference:
          name: "Research Conference 2021"
        contact:
          - name: "The RC21 Organizing Committee"
        copyright: "© 2021 The Research Software Project team"
        data-type: YAML
        database: "Research Database"
        database-provider:
          name: "Research Databases Ltd."
        date-accessed: "2021-07-27"
        date-downloaded: "2021-07-27"
        date-published: "2021-07-26"
        date-released: "2021-07-26"
        department: "Department of Hard Science Fiction"
        doi: 10.5281/zenodo.4813122
        edition: "2nd abridged edition"
        editors:
          - family-names: Inchief
            given-names: Editor
          - name: "The RCProc Editorial Team"
        editors-series:
          - family-names: Editor
            given-names: Series
          - name: "The Series Editors"
        end: 42
        entry: "Citation <n. 1>"
        filename: CITATION.cff
        format: "Citation File Format"
        identifiers:
          - description: "The concept DOI of the work."
            type: doi
            value: 10.5281/zenodo.1003149
          - description: "The versioned DOI for version 1.1.0 of the work."
            type: doi
            value: 10.5281/zenodo.4813122
          - description: "The Software Heritage identifier for version 1.1.0 of the work."
            type: swh
            value: "swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d"
          - description: "The GitHub release URL of tag 1.1.0."
            type: url
            value: "https://github.com/citation-file-format/citation-file-format/releases/tag/1.1.0"
        institution:
          name: "University of Arcadia"
        isbn: "9781603095075"
        issn: 2475-9066
        issue: 42
        issue-date: "November/December 2021"
        issue-title: "Special Issue: Software Citation"
        journal: "Journal of Open Source Software"
        keywords:
          - "software citation"
          - "citation file format"
          - research
        languages:
          - en
          - haw
        license: Apache-2.0
        license-url: "https://obscure-licenses.com?id=1234"
        loc-end: 42
        loc-start: 21
        location:
          name: "Library of the Unseen University"
        medium: "5¼-inch floppy disk"
        month: 7
        nihmsid: NIHMS236863
        notes: "Excellent reference! TODO Read for thesis."
        number: 12053
        number-volumes: 7
        pages: 78
        patent-states:
          - Canada
        pmcid: PMC3134971
        publisher:
          name: "Open Access Publishing House"
        recipients:
          - name: "Recipient entity of personal communication"
          - family-names: Recipient
            given-names: Communication
        repository: "https://ascl.net/2105.013"
        repository-artifact: "https://search.maven.org/artifact/org.corpus-tools/cff-maven-plugin/0.4.0/maven-plugin"
        repository-code: "https://github.com/citation-file-format/my-research-software"
        scope: "Supplement 2: Additional material"
        section: 7
        senders:
          - name: "Sender entity of personal communication"
          - family-names: Sender
            given-names: Communication
        start: 17
        status: submitted
        term: Citation
        thesis-type: "PhD thesis"
        title: "Towards better software citation"
        translators:
          - name: "Research Translators Ltd."
          - family-names: Lator
            given-names: Trans
        type: conference-paper
        url: "https://citation-file-format.github.io/"
        version: 0.3.12
        volume: 2
        volume-title: "Volume II: How it went on"
        year: 2021
        year-original: 1978
    ```

### `$defs.reference.abbreviation`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The abbreviation of a work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      abbreviation: ABC
      type: generic
    ```
    ```yaml
    references:
      - abbreviation: DEF
        type: generic
    ```

### `$defs.reference.abstract`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The abstract of the work.
    - If the work is a journal paper or other academic work: The abstract of the work.
    - If the work is a film, broadcast or similar: The synopsis of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      abstract: "This work describes the software or dataset that should be actually cited. etc."
      type: generic
    ```
    ```yaml
    references:
      - abstract: "This work implements an algorithm that we use in our software. etc."
        type: generic
    ```

### `$defs.reference.authors`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `true`
- **description**: The authors of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      authors:
        - name: "The Research Software Project team"
        - family-names: Druskat
          given-names: Stephan
      type: generic
    ```
    ```yaml
    references:
      - authors:
          - name: "The Research Software Project team"
          - family-names: Druskat
            given-names: Stephan
        type: generic
    ```

#### How to deal with unknown individual authors?

To enable credit for the individuals that have created a work,
it is good practice to cite the respective individuals as authors.
Sometimes you may not be able to determine the person names of the relevant individuals to create
[`$defs.person`](#defsperson) objects for them,
for example when a software you cite does not provide a `CITATION.cff` file.
Then, the next best thing is to refer to those that you could not determine person names for
collectively as a "team" or "project" using the title of the work
in a [`$defs.entity`](#defsentity) object:

```yaml
authors:
  - name: "The Research Software project"
```
```yaml
authors:
  - family-names: Spaaks
    given-names: "Jurriaan H."
  - family-names: Druskat
    given-names: Stephan
  - name: "The Research Software team"
```

This still represents the maximum knowledge you have about the authors.
It's also a good starting point to enable users of the citation metadata to determine the correct names themselves in the future,
especially if you also provide a source of information such as a `repository-code` or a `url`.

If the authors of a work are truly anonymous,
you can represent this in the same way:

```yaml
authors:
  - name: anonymous
```

### `$defs.reference.collection-doi`

- **type**: [`$defs.doi`](#defsdoi)
- **required**: `false`
- **description**: The [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) of a collection containing the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      collection-doi: 10.5281/zenodo.1003149
      type: generic
    ```
    ```yaml
    references:
      - collection-doi: 10.5281/zenodo.1003149
        type: generic
    ```

### `$defs.reference.collection-title`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The title of a collection or proceedings.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      collection-title: "Proceedings of the Research Conference 2021"
      type: generic
    ```
    ```yaml
    references:
      - collection-title: "Proceedings of the Research Conference 2021"
        type: generic
    ```

### `$defs.reference.collection-type`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The type of a collection.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      collection-type: proceedings
      type: generic
    ```
    ```yaml
    references:
      - collection-type: proceedings
        type: generic
    ```

### `$defs.reference.commit`

- **type**: [`$defs.commit`](#defscommit)
- **required**: `false`
- **description**: The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      commit: "16192bf05e99bcb35d5c3e085047807b5720fafc"
      type: generic
    ```
    ```yaml
    references:
      - commit: "16192bf05e99bcb35d5c3e085047807b5720fafc"
        type: generic
    ```

### `$defs.reference.conference`

- **type**: [`$defs.entity`](#defsentity)
- **required**: `false`
- **description**: The conference where the work was presented.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      conference:
        name: "Research Conference 2021"
      type: generic
    ```
    ```yaml
    references:
      - conference:
          name: "Research Conference 2021"
        type: generic
    ```

### `$defs.reference.contact`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The contact person, group, company, etc. for a work.
- **usage**:<br><br>
    ```yaml
    references:
      - contact:
        - name: "The RC21 Organizing Committee"
        - family-names: Druskat
          given-names: Stephan
        type: generic
    ```
    ```yaml
    preferred-citation:
      contact:
        - name: "The RC21 Organizing Committee"
        - family-names: Druskat
          given-names: Stephan
      type: generic
    ```

### `$defs.reference.copyright`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The copyright information pertaining to the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      copyright: "© 2021 The Research Software Project team"
      type: generic
    ```
    ```yaml
    references:
      - copyright: "© 2021 The Research Software Project team"
        type: generic
    ```

### `$defs.reference.data-type`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The data type of a data set.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      data-type: YAML
      type: generic
    ```
    ```yaml
    references:
      - data-type: YAML
        type: generic
    ```

### `$defs.reference.database-provider`

- **type**: [`$defs.entity`](#defsentity)
- **required**: `false`
- **description**: The provider of the database where a work was accessed/is stored.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      database-provider:
        name: "Research Databases Ltd."
      type: generic
    ```
    ```yaml
    references:
      - database-provider:
          name: "Research Databases Ltd."
        type: generic
    ```

### `$defs.reference.database`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The name of the database where a work was accessed/is stored.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      database: "Research Database"
      type: generic
    ```
    ```yaml
    references:
      - database: "Research Database"
        type: generic
    ```

### `$defs.reference.date-accessed`

- **type**: [`$defs.date`](#defsdate)
- **required**: `false`
- **description**: The date the work was accessed.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      date-accessed: "2021-07-27"
      type: generic
    ```
    ```yaml
    references:
      - date-accessed: "2021-07-27"
        type: generic
    ```

### `$defs.reference.date-downloaded`

- **type**: [`$defs.date`](#defsdate)
- **required**: `false`
- **description**: The date the work has been downloaded.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      date-downloaded: "2021-07-27"
      type: generic
    ```
    ```yaml
    references:
      - date-downloaded: "2021-07-27"
        type: generic
    ```

### `$defs.reference.date-published`

- **type**: [`$defs.date`](#defsdate)
- **required**: `false`
- **description**: The date the work has been published.
- **usage**:<br><br>
    ```yaml
    references:
      - date-published: "2021-07-27"
        type: generic
    ```
    ```yaml
    preferred-citation:
      date-published: "2021-07-27"
      type: generic
    ```

### `$defs.reference.date-released`

- **type**: [`$defs.date`](#defsdate)
- **required**: `false`
- **description**: The date the work has been released.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      date-released: "2021-07-27"
      type: generic
    ```
    ```yaml
    references:
      - date-released: "2021-07-27"
        type: generic
    ```

### `$defs.reference.department`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The department where a work has been produced.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      department: "Department of Hard Science Fiction"
      type: generic
    ```
    ```yaml
    references:
      - department: "Department of Hard Science Fiction"
        type: generic
    ```

### `$defs.reference.doi`

- **type**: [`$defs.doi`](#defsdoi)
- **required**: `false`
- **description**: The [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      doi: 10.5281/zenodo.4813122
      type: generic
    ```
    ```yaml
    references:
      - doi: 10.5281/zenodo.4813122
        type: generic
    ```

### `$defs.reference.edition`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The edition of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      edition: "2nd abridged edition"
      type: generic
    ```
    ```yaml
    references:
      - edition: "2nd abridged edition"
        type: generic
    ```

### `$defs.reference.editors`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The editor(s) of a work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      editors:
        - family-names: Inchief
          given-names: Editor
        - name: "The RCProc Editorial Team"
      type: generic
    ```
    ```yaml
    references:
      - editors:
        - family-names: Inchief
          given-names: Editor
        - name: "The RCProc Editorial Team"
        type: generic
    ```

### `$defs.reference.editors-series`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The editor(s) of a series in which a work has been published.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      editors-series:
        - family-names: Editor
          given-names: Series
        - name: "The Series Editors"
      type: generic
    ```
    ```yaml
    references:
      - editors-series:
        - family-names: Editor
          given-names: Series
        - name: "The Series Editors"
        type: generic
    ```

### `$defs.reference.end`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The end page of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      end: "42"
      type: generic
    ```
    ```yaml
    preferred-citation:
      end: 42
      type: generic
    ```
    ```yaml
    references:
      - end: "42"
        type: generic
    ```
    ```yaml
    references:
      - end: 42
        type: generic
    ```

### `$defs.reference.entry`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: An entry in the collection that constitutes the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      entry: "Citation <n. 1>"
      type: generic
    ```
    ```yaml
    references:
      - entry: "Citation <n. 1>"
        type: generic
    ```

### `$defs.reference.filename`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The name of the electronic file containing the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      filename: CITATION.cff
      type: generic
    ```
    ```yaml
    references:
      - filename: CITATION.cff
        type: generic
    ```

### `$defs.reference.format`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The format in which a work is represented.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      format: "Citation File Format"
      type: generic
    ```
    ```yaml
    references:
      - format: "Citation File Format"
        type: generic
    ```

### `$defs.reference.identifiers`

- **type**: Array of [`$defs.identifier`](#defsidentifier) objects.
- **required**: `false`
- **description**: The identifier(s) of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      identifiers:
        - description: "The concept DOI of the work."
          type: doi
          value: 10.5281/zenodo.1003149
        - description: "The versioned DOI for version 1.1.0 of the work."
          type: doi
          value: 10.5281/zenodo.4813122
        - description: "The Software Heritage identifier for version 1.1.0 of the work."
          type: swh
          value: "swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d"
        - description: "The GitHub release URL of tag 1.1.0."
          type: url
          value: "https://github.com/citation-file-format/citation-file-format/releases/tag/1.1.0"
      type: generic
    ```
    ```yaml
    references:
      - identifiers:
          - description: "The concept DOI of the work."
            type: doi
            value: 10.5281/zenodo.1003149
          - description: "The versioned DOI for version 1.1.0 of the work."
            type: doi
            value: 10.5281/zenodo.4813122
          - description: "The Software Heritage identifier for version 1.1.0 of the work."
            type: swh
            value: "swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d"
          - description: "The GitHub release URL of tag 1.1.0."
            type: url
            value: "https://github.com/citation-file-format/citation-file-format/releases/tag/1.1.0"
        type: generic
    ```

### `$defs.reference.institution`

- **type**: [`$defs.entity`](#defsentity)
- **required**: `false`
- **description**: The institution where a work has been produced or published.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      institution:
        name: "University of Arcadia"
      type: generic
    ```
    ```yaml
    references:
      - institution:
          name: "University of Arcadia"
        type: generic
    ```

### `$defs.reference.isbn`

- **type**: `string` with pattern [`^[0-9\- ]{10,17}X?$`](https://regex101.com/library/6oS1PA)
- **required**: `false`
- **description**: The [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      isbn: "9781603095075"
      type: generic
    ```
    ```yaml
    references:
      - isbn: "9781603095075"
        type: generic
    ```

### `$defs.reference.issn`

- **type**: `string` with pattern [`^\d{4}-\d{3}[\dxX]$`](https://regex101.com/library/jqobq9)
- **required**: `false`
- **description**: The [ISSN](https://en.wikipedia.org/wiki/International_Standard_Serial_Number) of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issn: "2475-9066"
      type: generic
    ```
    ```yaml
    references:
      - issn: "2475-9066"
        type: generic
    ```

### `$defs.reference.issue`

- **type**: [strictish string](#defsstrictish-string) or `number`
- **required**: `false`
- **description**: The issue of a periodical in which a work appeared.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issue: "42"
      type: generic
    ```
    ```yaml
    references:
      - issue: "42"
        type: generic
    ```
    ```yaml
    preferred-citation:
      issue: 42
      type: generic
    ```
    ```yaml
    references:
      - issue: 42
        type: generic
    ```

### `$defs.reference.issue-date`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The publication date of the issue of a periodical in which a work appeared.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issue-date: "November/December 2021"
      type: generic
    ```
    ```yaml
    references:
      - issue-date: "November/December 2021"
        type: generic
    ```
    ```yaml
    preferred-citation:
      issue-date: "2021-12-31"
      type: generic
    ```
    ```yaml
    references:
      - issue-date: "2021-12-31"
        type: generic
    ```

### `$defs.reference.issue-title`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The name of the issue of a periodical in which the work appeared.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issue-title: "Special Issue: Software Citation"
      type: generic
    ```
    ```yaml
    references:
      - issue-title: "Special Issue: Software Citation"
        type: generic
    ```

### `$defs.reference.journal`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The name of the journal/magazine/newspaper/periodical where the work was published.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      journal: "Journal of Open Source Software"
      type: generic
    ```
    ```yaml
    references:
      - journal: "Journal of Open Source Software"
        type: generic
    ```

### `$defs.reference.keywords`

- **type**: Array of [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: Keywords pertaining to the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      keywords:
        - "software citation"
        - "citation file format"
        - research
      type: generic
    ```
    ```yaml
    references:
      - keywords:
          - "software citation"
          - "citation file format"
          - research
        type: generic
    ```

### `$defs.reference.languages`

- **type**: Array of [ISO 639](https://en.wikipedia.org/wiki/ISO_639) `string` with 2 or 3 characters and pattern [`^[a-z]{2,3}$`](https://regex101.com/library/aMqWLH)
- **required**: `false`
- **description**: The language identifier(s) of the work according to ISO 639 language strings.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      languages:
        - en
        - haw
      type: generic
    ```
    ```yaml
    references:
      - languages:
          - en
          - haw
        type: generic
    ```

### `$defs.reference.license`

- **type**: (Array of) [`$defs.license-enum`](#defslicense-enum).
- **required**: `false`
- **description**: The [SPDX license identifier(s)](https://spdx.dev/ids/) for the license(s) under which the work is made available.
When there are multiple licenses, it is assumed their relationship is OR, not AND.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      license: Apache-2.0
      type: generic
    ```
    ```yaml
    references:
      - license: Apache-2.0
        type: generic
    ```
    ```yaml
    preferred-citation:
      license:
        - Apache-2.0
        - MIT
      type: generic
    ```
    ```yaml
    references:
      - license:
          - Apache-2.0
          - MIT
        type: generic
    ```

### `$defs.reference.license-url`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the license text under which the work is licensed (only for non-standard licenses not included in the [SPDX License List](#defslicense-enum)).
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      license-url: "https://obscure-licenses.com?id=1234"
      type: generic
    ```
    ```yaml
    references:
      - license-url: "https://obscure-licenses.com?id=1234"
        type: generic
    ```

### `$defs.reference.loc-end`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The line of code in the file where the work ends.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      loc-end: "42"
      type: generic
    ```
    ```yaml
    preferred-citation:
      loc-end: 42
      type: generic
    ```
    ```yaml
    references:
      - loc-end: "42"
        type: generic
    ```
    ```yaml
    references:
      - loc-end: 42
        type: generic
    ```

### `$defs.reference.loc-start`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The line of code in the file where the work starts.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      loc-start: "21"
      type: generic
    ```
    ```yaml
    preferred-citation:
      loc-start: 21
      type: generic
    ```
    ```yaml
    references:
      - loc-start: "21"
        type: generic
    ```
    ```yaml
    references:
      - loc-start: 21
        type: generic
    ```

### `$defs.reference.location`

- **type**: [`$defs.entity`](#defsentity)
- **required**: `false`
- **description**: The location of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      location:
        name: "Library of the Unseen University"
      type: generic
    ```
    ```yaml
    references:
      - location:
          name: "Library of the Unseen University"
        type: generic
    ```

### `$defs.reference.medium`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The medium of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      medium: "5¼-inch floppy disk"
      type: generic
    ```
    ```yaml
    references:
      - medium: "5¼-inch floppy disk"
        type: generic
    ```

### `$defs.reference.month`

- **type**: `integer` in range `1-12` or `enum` with values:
    - `1`
    - `2`
    - `3`
    - `4`
    - `5`
    - `6`
    - `7`
    - `8`
    - `9`
    - `10`
    - `11`
    - `12`
- **required**: `false`
- **description**: The month in which a work has been published.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      month: 7
      type: generic
    ```
    ```yaml
    preferred-citation:
      month: "7"
      type: generic
    ```
    ```yaml
    references:
      - month: 7
        type: generic
    ```
    ```yaml
    references:
      - month: "7"
        type: generic
    ```

### `$defs.reference.nihmsid`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The [NIHMSID](https://web.archive.org/web/20210802210057/https://www.ncbi.nlm.nih.gov/pmc/about/public-access-info/) of a work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      nihmsid: NIHMS236863
      type: generic
    ```
    ```yaml
    references:
      - nihmsid: NIHMS236863
        type: generic
    ```

### `$defs.reference.notes`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: Notes pertaining to the work. Note that this key should contain notes that may be picked up by some downstream tooling (e.g., reference managers), but not others (e.g., a software index).
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      notes: "Excellent reference! TODO Read for thesis."
      type: generic
    ```
    ```yaml
    references:
      - notes: "Excellent reference! TODO Read for thesis."
        type: generic
    ```

### `$defs.reference.number`

- **type**: `string` or `number`
- **required**: `false`
- **description**: The number of a work, e.g., an article identifier (such as *86* or *e86* for [this paper](https://doi.org/10.7717/peerj-cs.86)) or a (library) [accession number](https://en.wikipedia.org/wiki/Accession_number).
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      number: "005.1-ABC"
      type: generic
    ```
    ```yaml
    references:
      - number: "005.1-ABC"
        type: generic
    ```
    ```yaml
    preferred-citation:
      number: 1234567
      type: generic
    ```
    ```yaml
    references:
      - number: 1234567
        type: generic
    ```
    ```yaml
    preferred-citation:
      number: 1.4
      type: generic
    ```
    ```yaml
    references:
      - number: 1.4
        type: generic
    ```

### `$defs.reference.number-volumes`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The number of volumes making up the collection in which the work has been published.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      number-volumes: "4"
      type: generic
    ```
    ```yaml
    preferred-citation:
      number-volumes: 4
      type: generic
    ```
    ```yaml
    references:
      - number-volumes: "4"
        type: generic
    ```
    ```yaml
    references:
      - number-volumes: 4
        type: generic
    ```

### `$defs.reference.pages`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The number of pages of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      pages: "123"
      type: generic
    ```
    ```yaml
    preferred-citation:
      pages: 123
      type: generic
    ```
    ```yaml
    references:
      - pages: "123"
        type: generic
    ```
    ```yaml
    references:
      - pages: 123
        type: generic
    ```

### `$defs.reference.patent-states`

- **type**: Array of nonemtpy `string`
- **required**: `false`
- **description**: The states for which a patent is granted.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      patent-states:
        - Canada
        - IL
      type: generic
    ```
    ```yaml
    references:
      - patent-states:
          - Canada
          - IL
        type: generic
    ```

### `$defs.reference.pmcid`

- **type**: `string` with pattern [`^PMC[0-9]{7,8}$`](https://regex101.com/library/lMDdvW)
- **required**: `false`
- **description**: The [PMCID](https://web.archive.org/web/20210802210057/https://www.ncbi.nlm.nih.gov/pmc/about/public-access-info/) of a work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      pmcid: PMC3134971
      type: generic
    ```
    ```yaml
    references:
      - pmcid: PMC3134971
        type: generic
    ```

### `$defs.reference.publisher`

- **type**: [`$defs.entity`](#defsentity)
- **required**: `false`
- **description**: The publisher who has published the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      publisher:
        name: "Open Access Publishing House"
      type: generic
    ```
    ```yaml
    references:
      - publisher:
          name: "Open Access Publishing House"
        type: generic
    ```

### `$defs.reference.recipients`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The recipient(s) of a personal communication.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      recipients:
        - name: "Recipient entity of personal communication"
        - family-names: Recipient
          given-names: Communication
      type: generic
    ```
    ```yaml
    references:
      - recipients:
          - name: "Recipient entity of personal communication"
          - family-names: Recipient
            given-names: Communication
        type: generic
    ```

### `$defs.reference.repository`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the work in a repository/archive (when the repository is neither a source code repository nor a build artifact repository).
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      repository: "https://ascl.net/2105.013"
      type: generic
    ```
    ```yaml
    references:
      - repository: "https://ascl.net/2105.013"
        type: generic
    ```

### `$defs.reference.repository-artifact`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the work in a build artifact/binary repository.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      repository-artifact: "https://search.maven.org/artifact/org.corpus-tools/cff-maven-plugin/0.4.0/maven-plugin"
      type: generic
    ```
    ```yaml
    references:
      - repository-artifact: "https://search.maven.org/artifact/org.corpus-tools/cff-maven-plugin/0.4.0/maven-plugin"
        type: generic
    ```

### `$defs.reference.repository-code`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the work in a source code repository.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      repository-code: "https://github.com/citation-file-format/my-research-software"
      type: generic
    ```
    ```yaml
    references:
      - repository-code: "https://github.com/citation-file-format/my-research-software"
        type: generic
    ```

### `$defs.reference.scope`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The scope of the reference, e.g., the section of the work it adheres to.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      scope: "Supplement 2: Additional material"
      type: generic
    ```
    ```yaml
    references:
      - scope: "Supplement 2: Additional material"
        type: generic
    ```

### `$defs.reference.section`

- **type**: `string` or `number`
- **required**: `false`
- **description**: The section of a work that is referenced.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      section: "Section 7: Software citation"
      type: generic
    ```
    ```yaml
    references:
      - section: "Section 7: Software citation"
        type: generic
    ```
    ```yaml
    preferred-citation:
      section: 7
      type: generic
    ```
    ```yaml
    references:
      - section: 7
        type: generic
    ```
    ```yaml
    preferred-citation:
      section: 7.1
      type: generic
    ```
    ```yaml
    references:
      - section: 7.1
        type: generic
    ```

### `$defs.reference.senders`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The sender(s) of a personal communication.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      senders:
        - name: "Sender entity of personal communication"
        - family-names: Sender
          given-names: Communication
      type: generic
    ```
    ```yaml
    references:
      - senders:
          - name: "Sender entity of personal communication"
          - family-names: Sender
            given-names: Communication
        type: generic
    ```

### `$defs.reference.start`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The start page of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      start: "42"
      type: generic
    ```
    ```yaml
    preferred-citation:
      start: 42
      type: generic
    ```
    ```yaml
    references:
      - start: "42"
        type: generic
    ```
    ```yaml
    references:
      - start: 42
        type: generic
    ```

### `$defs.reference.status`

- **type**: `enum` with values:
    - `abstract`
    - `advance-online`
    - `in-preparation`
    - `in-press`
    - `preprint`
    - `submitted`
- **required**: `false`
- **description**: The publication status of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      status: submitted
      type: generic
    ```
    ```yaml
    references:
      - status: submitted
        type: generic
    ```

### `$defs.reference.term`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The term being referenced if the work is a dictionary or encyclopedia.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      term: Citation
      type: generic
    ```
    ```yaml
    references:
      - term: Citation
        type: generic
    ```

### `$defs.reference.thesis-type`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The type of the thesis that is the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      thesis-type: "PhD thesis"
      type: generic
    ```
    ```yaml
    references:
      - thesis-type: "PhD thesis"
        type: generic
    ```

### `$defs.reference.title`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `true`
- **description**: The title of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      title: "Towards better software citation"
      type: generic
    ```
    ```yaml
    references:
      - title: "Towards better software citation"
        type: generic
    ```

### `$defs.reference.translators`

- **type**: Array of [`$defs.person`](#defsperson) and/or [`$defs.entity`](#defsentity) objects.
- **required**: `false`
- **description**: The translator(s) of a work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      translators:
        - name: "Research Translators Ltd."
        - family-names: Lator
          given-names: Trans
      type: generic
    ```
    ```yaml
    references:
      - translators:
          - name: "Research Translators Ltd."
          - family-names: Lator
            given-names: Trans
        type: generic
    ```

### `$defs.reference.type`

- **type**: `enum` with values:
    - `art`
    - `article`
    - `audiovisual`
    - `bill`
    - `blog`
    - `book`
    - `catalogue`
    - `conference-paper`
    - `conference`
    - `data`
    - `database`
    - `dictionary`
    - `edited-work`
    - `encyclopedia`
    - `film-broadcast`
    - `generic`
    - `government-document`
    - `grant`
    - `hearing`
    - `historical-work`
    - `legal-case`
    - `legal-rule`
    - `magazine-article`
    - `manual`
    - `map`
    - `multimedia`
    - `music`
    - `newspaper-article`
    - `pamphlet`
    - `patent`
    - `personal-communication`
    - `proceedings`
    - `report`
    - `serial`
    - `slides`
    - `software-code`
    - `software-container`
    - `software-executable`
    - `software-virtual-machine`
    - `software`
    - `sound-recording`
    - `standard`
    - `statute`
    - `thesis`
    - `unpublished`
    - `video`
    - `website`
- **required**: `true`
- **description**: The type of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
        type: generic
    ```
    ```yaml
    references:
      - type: generic
    ```

### `$defs.reference.url`

- **type**: [`$defs.url`](#defsurl)
- **required**: `false`
- **description**: The URL of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      url: "https://citation-file-format.github.io/"
    ```
    ```yaml
    references:
      - type: generic
        url: "https://citation-file-format.github.io/"
    ```

### `$defs.reference.version`

- **type**: [`$defs.version`](#defsversion)
- **required**: `false`
- **description**: The version of the work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      version: 0.3.12
    ```
    ```yaml
    references:
      - type: generic
        version: 0.3.12
    ```

### `$defs.reference.volume`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The volume of the periodical in which a work appeared.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      volume: "5"
    ```
    ```yaml
    preferred-citation:
      type: generic
      volume: 5
    ```
    ```yaml
    references:
      - type: generic
        volume: "5"
    ```
    ```yaml
    references:
      - type: generic
        volume: 5
    ```

### `$defs.reference.volume-title`

- **type**: [strictish string](#defsstrictish-string)
- **required**: `false`
- **description**: The title of the volume in which the work appeared.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      volume-title: "Volume II: How it went on"
    ```
    ```yaml
    references:
      - type: generic
        volume-title: "Volume II: How it went on"
    ```

### `$defs.reference.year`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The year in which a work has been published.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      year: "2021"
    ```
    ```yaml
    preferred-citation:
      type: generic
      year: 2021
    ```
    ```yaml
    references:
      - type: generic
        year: "2021"
    ```
    ```yaml
    references:
      - type: generic
        year: 2021
    ```

### `$defs.reference.year-original`

- **type**: [strictish string](#defsstrictish-string) or `integer`
- **required**: `false`
- **description**: The year of the original publication.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      year-original: "1978"
    ```
    ```yaml
    preferred-citation:
      type: generic
      year-original: 1978
    ```
    ```yaml
    references:
      - type: generic
        year-original: "1978"
    ```
    ```yaml
    references:
      - type: generic
        year-original: 1978
    ```

### `$defs.region`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A region.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project"
        region: Renfrewshire
    ```

### `$defs.ror`

- **type**: string of length 25 with pattern `^https://ror.org/0[0-9|a-z]{8}$`
- **required**: `false`
- **description**: The entity's Research Organization Registry identifier, see https://ror.org.
- **usage**:<br><br>
    ```yaml
    authors:
    - name: German Aerospace Center
      ror: https://ror.org/04bwf3e34
    - name: Netherlands eScience Center
      ror: https://ror.org/00rbjv475
    ```

### `$defs.strictish-string`

- **type**: `string` with pattern [`"^(\\S+)( \\S+)*$"`](https://regex101.com/r/SyW84W/1)
- **required**: N/A
- **description**: Nonempty string without any leading spaces, trailing spaces or double spaces.
- **usage**:<br><br>
    ```yaml
    abstract: This is the abstract. It can't have leading spaces, trailing spaces, or doubles spaces.
    ```

### `$defs.swh-identifier`

- **type**: `string` with pattern [`^swh:1:(snp|rel|rev|dir|cnt):[0-9a-fA-F]{40}$`](https://regex101.com/library/o399MX)
- **required**: N/A
- **description**: The [Software Heritage](https://www.softwareheritage.org/) identifier (without further qualifiers such as origin, visit, anchor, path). Note: Software Heritage identifiers are documented here: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html.
- **usage**:<br><br>
    ```yaml
    identifiers:
      - type: swh
        value: "swh:1:rev:309cf2674ee7a0749978cf8265ab91a60aea0f7d"
    ```

### `$defs.tel`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A telephone number.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        tel: +12-345-6789098
    ```
    ```yaml
    authors:
      - name: "The Research Software Project"
        tel: +12-345-6789098
    ```

### `$defs.url`

- **type**: [strictish string](#defsstrictish-string)
- **required**: N/A
- **description**: A URL. Supported URLs start with one of:
    - `https://`
    - `http://`
    - `ftp://`
    - `sftp://`
- **usage**
    ```yaml
    url: "https://citation-file-format.github.io/"
    ```
    ```yaml
    authors:
      - name: "The Research Software Project"
        website: "https://research-software-project.org"
    ```
    ```yaml
    references:
      - type: generic
        url: "sftp://files.research-software-project.org"
    ```

### `$defs.version`

- **type**: [strictish string](#defsstrictish-string) or `number`
- **required**: N/A
- **description**: The version of a work.
- **usage**:<br><br>
    ```yaml
    version: "7.2.0"
    ```
    ```yaml
    version: 7.2
    ```
    ```yaml
    version: "21.10 (Impish Indri)"
    ```
