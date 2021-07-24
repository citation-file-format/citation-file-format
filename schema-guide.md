# Guide to Citation File Format schema version 1.2.0

## General structure of a `CITATION.cff` file

Valid Citation File Format files

1. must be named `CITATION.cff` (note the capitalization)
1. are valid YAML 1.2
1. are valid according to the Citation File Format schema version 1.2.0 outlined in [schema.json](schema.json)

### Minimal example

A minimal example of a valid `CITATION.cff` file could look like this:

```yaml
authors:
  -
    family-names: Druskat
    given-names: Stephan
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
title: My Research Software
```

### Typical example

For most software however, it is relatively easy to expand the minimal case with some more information like the version, the date when it was last published, some keywords, etc.:

```yaml
abstract: This is my awesome research software. It does many things.
authors: 
  -
    family-names: Druskat
    given-names: Stephan
    orcid: "https://orcid.org/0000-0003-4925-7248"
cff-version: 1.2.0
date-released: "2021-07-18"
identifiers: 
  - 
    description: This is the collection of archived snapshots of all versions of My Research Software
    type: doi
    value: "10.5281/zenodo.123456"
  - 
    description: This is the archived snapshot of version 0.11.2 of My Research Software
    type: doi
    value: "10.5281/zenodo.123457"
keywords: 
  - "awesome software"
  - research
license: Apache-2.0
message: If you use this software, please cite it using these metadata.
repository-code: "https://github.com/citation-file-format/my-research-software"
title: My Research Software
version: 0.11.2
```

### Transitive credit

When your software or data builds on what others have already done, it is good practice to add a `references` section to your
`CITATION.cff` file. This way, whenever your work gets credited, a little bit of that goes into crediting the works that
you built on.

```yaml
authors:
  -
    family-names: Druskat
    given-names: Stephan
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
title: My Research Software
references:
  authors:
    - 
      family-names: Spaaks
      given-names: Jurriaan H.
  title: The foundation of Research Software
  type: software
```


### Credit redirection

Sometimes you want to redirect any credit your work may receive towards a second work (typically one of your own). A
common example is when you write software and then write a paper about it, you may want be credited for the paper
instead of for the software itself. In that case, your `CITATION.cff` should contain some metadata about the software at
the root of the `CITATION.cff` file, but additionally, there should be a `preferred-citation` key with the metadata of
the redirection target. Usually, the `message` also reflects the authors' wishes on how they want to be credited.

```yaml
authors:
  -
    family-names: Druskat
    given-names: Stephan
cff-version: 1.2.0
message: If you use this software, please cite the article from preferred-citation instead of the software.
title: My Research Software
preferred-citation:
  authors:
    - 
      family-names: Druskat
      given-names: Stephan
  title: Software paper about My Research Software
  type: article
```

The next sections explain each key in more detail.

## root-level keys

This section aims to describe what keys are valid at the root level of a `CITATION.cff` file.

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

- type: `string`
- required: `false`

A description of the software or dataset.

Usage example:

```yaml
abstract: This software implements methods to do things.
```

### `authors`

- type: Array of [`definitions.person`](#definitionsperson) and/or [`definitions.entity`](#definitionsentity) objects.
- required: `true`

The authors of a software or dataset.

Usage example:

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

- type: `string`
- required: `true`

The Citation File Format schema version that the `CITATION.cff` file adheres to for providing the citation metadata.

Usage example:

```yaml
cff-version: 1.2.0
```
```yaml
cff-version: "1.2.0"
```

### `commit`

- type: `string`
- required: `false`

The commit hash or revision number of the software version.

Usage example:

```yaml
commit: 1ff847d81f29c45a3a1a5ce73d38e45c2f319bba
```
```yaml
commit: "Revision: 8612"
```

### `contact`

- type: Array of [`definitions.person`](#definitionsperson) and/or [`definitions.entity`](#definitionsentity) objects.
- required: `false`

The contact person, group, company, etc. for the software or dataset.

Usage example:

```yaml
contact:
  - affiliation: "Humboldt-Universität zu Berlin"
    email: "mail@sdruskat.net"
    family-names: Druskat
    given-names: Stephan
```
```yaml
contact:
  - email: "mail@research-project.org"
    name: "The Research Software project"
```
```yaml
contact:
  - email: "mail@sdruskat.net"
    given-names: Stephan
    family-names: Druskat
  - email: "mail@research-project.org"
    name: "The Research Software project"
```

### `date-released`

- type: [`definitions.date`](#definitionsdate)
- required: `false`

The date the software or data set has been released. Format is 4-digit year, 2-digit month, 2-digit day of month, separated by dashes.

Usage example:

```yaml
date-released: 2020-01-31
```

### `doi`

- type: [`definitions.doi`](#definitionsdoi)
- required: `false`

The DOI of the software or data set. This notation is most useful when there is just one DOI you want to include. In
that case, `doi` can be used as shorthand for something like:

```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.1003149
    description: The concept DOI of the work.
```
or

```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.4813122
    description: The versioned DOI of the work.
```

Usage example:

```yaml
doi: 10.5281/zenodo.1003149
```
```yaml
doi: 10.5281/zenodo.4813122
```

### `identifiers`

- type: array of [`definitions.identifier`](#definitionsidentifier) objects.
- required: `false`

The identifiers of the software or dataset.

Usage example: see [`definitions.identifier`](#definitionsidentifier).

### `keywords`

- type: array of `string`
- required: `false`

Keywords that describe the work.

Usage example:

```yaml
keywords:
 - thefirstkeyword
 - thesecondkeyword
 - and a third
```

### `license`

- type: (array of) [`definitions.license-enum`](#definitionslicense-enum).
- required: `false`

The SPDX license identifier(s) for the license(s) under which the work is made available. When there are multiple
licenses, it is assumed their relationship is OR, not AND.

Usage example:

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

- type: [`definitions.url`](#definitionsurl)
- required: `false`

The URL of the license text under which the software or dataset is licensed (only for non-standard licenses not included in the SPDX License List).

Usage example:

```yaml
license-url: "https://obscure-licenses.com?id=1234"
```

### `message`

- type: `string`
- required: `true`
- default: `If you use this software, please cite it using the metadata from this file.`

A message to the human reader of the CITATION.cff file to let them know what to do with the citation metadata.

Usage example:

```yaml
message: If you use this software, please cite it using the metadata from this file.
```
```yaml
message: Please cite this software using these metadata.
```
```yaml
message: Please cite this software using the metadata from 'preferred-citation'.
```
```yaml
message: If you use this data set, please cite it using the metadata from this file.
```
```yaml
message: Please cite this data set using these metadata.
```
```yaml
message: Please cite this data set using the metadata from 'preferred-citation'.
```

### `preferred-citation`

- type: A [`definitions.reference`](#definitionsreference) object. 
- required: `false`

...

Usage example:

```yaml
preferred-citation:
  authors:
    - 
      family-names: Famnames
      given-names: Given Nam E. 
  title: Title of the work.
  type: generic
  year: 2021
```

### `references`

Array of [`definitions.reference`](#definitionsreference) objects.

### `repository`

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `repository-artifact`

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `repository-code`

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `title`

- type: `...`
- required: `true`

...

Usage example:

```yaml
```

### `type`

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `url`

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `version`

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

## Definitions

TODO explain why we use definitions

### Index

- [`definitions.address`](#definitionsaddress)
- [`definitions.alias`](#definitionsalias)
- [`definitions.city`](#definitionscity)
- [`definitions.commit`](#definitionscommit)
- [`definitions.country`](#definitionscountry)
- [`definitions.date`](#definitionsdate)
- [`definitions.doi`](#definitionsdoi)
- [`definitions.email`](#definitionsemail)
- [`definitions.entity`](#definitionsentity) (object)
- [`definitions.fax`](#definitionsfax)
- [`definitions.identifier`](#definitionsidentifier) (object)
- [`definitions.identifier-description`](#definitionsidentifier-description)
- [`definitions.license`](#definitionslicense)
- [`definitions.license-enum`](#definitionslicense-enum)
- [`definitions.orcid`](#definitionsorcid)
- [`definitions.person`](#definitionsperson) (object)
- [`definitions.post-code`](#definitionspost-code)
- [`definitions.reference`](#definitionsreference) (object)
- [`definitions.region`](#definitionsregion)
- [`definitions.swh-identifier`](#definitionsswh-identifier)
- [`definitions.tel`](#definitionstel)
- [`definitions.url`](#definitionsurl)
- [`definitions.version`](#definitionsversion)

### `definitions.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty `string`
- required: `false`

An address.


Usage example:

```yaml
```

### `definitions.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty `string`
- required: `false`

An alias.

Usage example:

```yaml
```

### `definitions.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty `string`
- required: `false`

A city.

Usage example:

```yaml
```

### `definitions.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty `string`
- required: `false`

The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.

Usage example:

```yaml
```

### `definitions.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `enum`
- required: `false`

The ISO 3166-1 alpha-2 country code for a country.

Usage example:

```yaml
country: NL
```
```yaml
country: DE
```

### `definitions.date`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `string`
- required: `false`

A date. Format is 4-digit year, 2-digit month, 2-digit day of month, separated by dashes.

Usage examples:

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
  - date-end: "2020-02-02"
    date-start: "2020-01-31"
    type: conference
```
```yaml
references:
  - issue-date: "2020-02-02"
    type: article
```

Note to tool implementers: it is necessary to cast YAML date objects to string objects when validating against the schema.

### `definitions.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `string`
- required: `false`

The DOI of the work (i.e., `10.5281/zenodo.1003150`, not the resolver URL `http://doi.org/10.5281/zenodo.1003150`).

Usage example:

```yaml
doi: "10.5281/zenodo.1003150"
```

### `definitions.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `string`
- required: `false`

An email address

Usage example:

```yaml
```

### `definitions.entity`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `object`
- required: `false`

...

`definitions.entity` has the following properties:

- [`address`](#definitionsentityaddress)
- [`alias`](#definitionsentityalias)
- [`city`](#definitionsentitycity)
- [`country`](#definitionsentitycountry)
- [`date-end`](#definitionsentitydate-end)
- [`date-start`](#definitionsentitydate-start)
- [`email`](#definitionsentityemail)
- [`fax`](#definitionsentityfax)
- [`location`](#definitionsentitylocation)
- [`name`](#definitionsentityname)
- [`orcid`](#definitionsentityorcid)
- [`post-code`](#definitionsentitypost-code)
- [`region`](#definitionsentityregion)
- [`tel`](#definitionsentitytel)
- [`website`](#definitionsentitywebsite)

### `definitions.entity.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.address`](#definitionsaddress).

The entity's address.

### `definitions.entity.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.alias`](#definitionsalias).

The entity's alias.

### `definitions.entity.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.city`](#definitionscity).

The entity's city.

### `definitions.entity.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.country`](#definitionscountry).

The entity's country.

### `definitions.entity.date-end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.date`](#definitionsdate).

The entity's ending date, e.g. when the entity is a conference.

### `definitions.entity.date-start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.date`](#definitionsdate).

The entity's starting date, e.g. when the entity is a conference.

### `definitions.entity.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.email`](#definitionsemail).

The entity's email address.

### `definitions.entity.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.fax`](#definitionsfax).

The entity's fax number.

### `definitions.entity.location`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.entity.name`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `true`

...

Usage example:

```yaml
```

### `definitions.entity.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.orcid`](#definitionsorcid).

The entity's orcid.

### `definitions.entity.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.post-code`](#definitionspost-code).

The entity's post code.

### `definitions.entity.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.region`](#definitionsregion).

The entity's region.

### `definitions.entity.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.tel`](#definitionstel).

The entity's telephone number.

### `definitions.entity.website`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

See [`definitions.url`](#definitionsurl).

The entity's website.

### `definitions.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:


```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.1003149
    description: The concept DOI of the work.
```
```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.4813122
    description: The versioned DOI for version 1.1.0 of the work.
```
```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.1003149
    description: The concept DOI of the work.
  - type: doi
    value: 10.5281/zenodo.4813122
    description: The versioned DOI for version 1.1.0 of the work.
```
```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.1003149
    description: The concept DOI of the work.
  - type: doi
    value: 10.5281/zenodo.4813122
    description: The versioned DOI for version 1.1.0 of the work.
  - type: swh
    value: swh:1:dir:bc286860f423ea7ced246ba7458eef4b4541cf2d
    description: The Software Heritage identifier for version 1.1.0 of the work.
  - type: url
    value: https://github.com/citation-file-format/citation-file-format/releases/tag/1.1.0
    description: The GitHub release URL to tag 1.1.0.
  - type: url
    value: https://github.com/citation-file-format/citation-file-format/tree/16192bf05e99bcb35d5c3e085047807b5720fafc
    description: The GitHub release URL to the commit of tag 1.1.0.
```

### `definitions.identifier-description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.license-enum`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `enum` with values:
    1. `0BSD`
    1. `AAL`
    1. `Abstyles`
    1. `Adobe-2006`
    1. `Adobe-Glyph`
    1. `ADSL`
    1. `AFL-1.1`
    1. `AFL-1.2`
    1. `AFL-2.0`
    1. `AFL-2.1`
    1. `AFL-3.0`
    1. `Afmparse`
    1. `AGPL-1.0`
    1. `AGPL-1.0-only`
    1. `AGPL-1.0-or-later`
    1. `AGPL-3.0`
    1. `AGPL-3.0-only`
    1. `AGPL-3.0-or-later`
    1. `Aladdin`
    1. `AMDPLPA`
    1. `AML`
    1. `AMPAS`
    1. `ANTLR-PD`
    1. `ANTLR-PD-fallback`
    1. `Apache-1.0`
    1. `Apache-1.1`
    1. `Apache-2.0`
    1. `APAFML`
    1. `APL-1.0`
    1. `APSL-1.0`
    1. `APSL-1.1`
    1. `APSL-1.2`
    1. `APSL-2.0`
    1. `Artistic-1.0`
    1. `Artistic-1.0-cl8`
    1. `Artistic-1.0-Perl`
    1. `Artistic-2.0`
    1. `Bahyph`
    1. `Barr`
    1. `Beerware`
    1. `BitTorrent-1.0`
    1. `BitTorrent-1.1`
    1. `blessing`
    1. `BlueOak-1.0.0`
    1. `Borceux`
    1. `BSD-1-Clause`
    1. `BSD-2-Clause`
    1. `BSD-2-Clause-FreeBSD`
    1. `BSD-2-Clause-NetBSD`
    1. `BSD-2-Clause-Patent`
    1. `BSD-2-Clause-Views`
    1. `BSD-3-Clause`
    1. `BSD-3-Clause-Attribution`
    1. `BSD-3-Clause-Clear`
    1. `BSD-3-Clause-LBNL`
    1. `BSD-3-Clause-Modification`
    1. `BSD-3-Clause-No-Nuclear-License`
    1. `BSD-3-Clause-No-Nuclear-License-2014`
    1. `BSD-3-Clause-No-Nuclear-Warranty`
    1. `BSD-3-Clause-Open-MPI`
    1. `BSD-4-Clause`
    1. `BSD-4-Clause-Shortened`
    1. `BSD-4-Clause-UC`
    1. `BSD-Protection`
    1. `BSD-Source-Code`
    1. `BSL-1.0`
    1. `BUSL-1.1`
    1. `bzip2-1.0.5`
    1. `bzip2-1.0.6`
    1. `C-UDA-1.0`
    1. `CAL-1.0`
    1. `CAL-1.0-Combined-Work-Exception`
    1. `Caldera`
    1. `CATOSL-1.1`
    1. `CC-BY-1.0`
    1. `CC-BY-2.0`
    1. `CC-BY-2.5`
    1. `CC-BY-3.0`
    1. `CC-BY-3.0-AT`
    1. `CC-BY-3.0-US`
    1. `CC-BY-4.0`
    1. `CC-BY-NC-1.0`
    1. `CC-BY-NC-2.0`
    1. `CC-BY-NC-2.5`
    1. `CC-BY-NC-3.0`
    1. `CC-BY-NC-4.0`
    1. `CC-BY-NC-ND-1.0`
    1. `CC-BY-NC-ND-2.0`
    1. `CC-BY-NC-ND-2.5`
    1. `CC-BY-NC-ND-3.0`
    1. `CC-BY-NC-ND-3.0-IGO`
    1. `CC-BY-NC-ND-4.0`
    1. `CC-BY-NC-SA-1.0`
    1. `CC-BY-NC-SA-2.0`
    1. `CC-BY-NC-SA-2.5`
    1. `CC-BY-NC-SA-3.0`
    1. `CC-BY-NC-SA-4.0`
    1. `CC-BY-ND-1.0`
    1. `CC-BY-ND-2.0`
    1. `CC-BY-ND-2.5`
    1. `CC-BY-ND-3.0`
    1. `CC-BY-ND-4.0`
    1. `CC-BY-SA-1.0`
    1. `CC-BY-SA-2.0`
    1. `CC-BY-SA-2.0-UK`
    1. `CC-BY-SA-2.1-JP`
    1. `CC-BY-SA-2.5`
    1. `CC-BY-SA-3.0`
    1. `CC-BY-SA-3.0-AT`
    1. `CC-BY-SA-4.0`
    1. `CC-PDDC`
    1. `CC0-1.0`
    1. `CDDL-1.0`
    1. `CDDL-1.1`
    1. `CDL-1.0`
    1. `CDLA-Permissive-1.0`
    1. `CDLA-Sharing-1.0`
    1. `CECILL-1.0`
    1. `CECILL-1.1`
    1. `CECILL-2.0`
    1. `CECILL-2.1`
    1. `CECILL-B`
    1. `CECILL-C`
    1. `CERN-OHL-1.1`
    1. `CERN-OHL-1.2`
    1. `CERN-OHL-P-2.0`
    1. `CERN-OHL-S-2.0`
    1. `CERN-OHL-W-2.0`
    1. `ClArtistic`
    1. `CNRI-Jython`
    1. `CNRI-Python`
    1. `CNRI-Python-GPL-Compatible`
    1. `Condor-1.1`
    1. `copyleft-next-0.3.0`
    1. `copyleft-next-0.3.1`
    1. `CPAL-1.0`
    1. `CPL-1.0`
    1. `CPOL-1.02`
    1. `Crossword`
    1. `CrystalStacker`
    1. `CUA-OPL-1.0`
    1. `Cube`
    1. `curl`
    1. `D-FSL-1.0`
    1. `diffmark`
    1. `DOC`
    1. `Dotseqn`
    1. `DRL-1.0`
    1. `DSDP`
    1. `dvipdfm`
    1. `ECL-1.0`
    1. `ECL-2.0`
    1. `eCos-2.0`
    1. `EFL-1.0`
    1. `EFL-2.0`
    1. `eGenix`
    1. `Entessa`
    1. `EPICS`
    1. `EPL-1.0`
    1. `EPL-2.0`
    1. `ErlPL-1.1`
    1. `etalab-2.0`
    1. `EUDatagrid`
    1. `EUPL-1.0`
    1. `EUPL-1.1`
    1. `EUPL-1.2`
    1. `Eurosym`
    1. `Fair`
    1. `Frameworx-1.0`
    1. `FreeBSD-DOC`
    1. `FreeImage`
    1. `FSFAP`
    1. `FSFUL`
    1. `FSFULLR`
    1. `FTL`
    1. `GD`
    1. `GFDL-1.1`
    1. `GFDL-1.1-invariants-only`
    1. `GFDL-1.1-invariants-or-later`
    1. `GFDL-1.1-no-invariants-only`
    1. `GFDL-1.1-no-invariants-or-later`
    1. `GFDL-1.1-only`
    1. `GFDL-1.1-or-later`
    1. `GFDL-1.2`
    1. `GFDL-1.2-invariants-only`
    1. `GFDL-1.2-invariants-or-later`
    1. `GFDL-1.2-no-invariants-only`
    1. `GFDL-1.2-no-invariants-or-later`
    1. `GFDL-1.2-only`
    1. `GFDL-1.2-or-later`
    1. `GFDL-1.3`
    1. `GFDL-1.3-invariants-only`
    1. `GFDL-1.3-invariants-or-later`
    1. `GFDL-1.3-no-invariants-only`
    1. `GFDL-1.3-no-invariants-or-later`
    1. `GFDL-1.3-only`
    1. `GFDL-1.3-or-later`
    1. `Giftware`
    1. `GL2PS`
    1. `Glide`
    1. `Glulxe`
    1. `GLWTPL`
    1. `gnuplot`
    1. `GPL-1.0`
    1. `GPL-1.0-only`
    1. `GPL-1.0-or-later`
    1. `GPL-1.0+`
    1. `GPL-2.0`
    1. `GPL-2.0-only`
    1. `GPL-2.0-or-later`
    1. `GPL-2.0-with-autoconf-exception`
    1. `GPL-2.0-with-bison-exception`
    1. `GPL-2.0-with-classpath-exception`
    1. `GPL-2.0-with-font-exception`
    1. `GPL-2.0-with-GCC-exception`
    1. `GPL-2.0+`
    1. `GPL-3.0`
    1. `GPL-3.0-only`
    1. `GPL-3.0-or-later`
    1. `GPL-3.0-with-autoconf-exception`
    1. `GPL-3.0-with-GCC-exception`
    1. `GPL-3.0+`
    1. `gSOAP-1.3b`
    1. `HaskellReport`
    1. `Hippocratic-2.1`
    1. `HPND`
    1. `HPND-sell-variant`
    1. `HTMLTIDY`
    1. `IBM-pibs`
    1. `ICU`
    1. `IJG`
    1. `ImageMagick`
    1. `iMatix`
    1. `Imlib2`
    1. `Info-ZIP`
    1. `Intel`
    1. `Intel-ACPI`
    1. `Interbase-1.0`
    1. `IPA`
    1. `IPL-1.0`
    1. `ISC`
    1. `JasPer-2.0`
    1. `JPNIC`
    1. `JSON`
    1. `LAL-1.2`
    1. `LAL-1.3`
    1. `Latex2e`
    1. `Leptonica`
    1. `LGPL-2.0`
    1. `LGPL-2.0-only`
    1. `LGPL-2.0-or-later`
    1. `LGPL-2.0+`
    1. `LGPL-2.1`
    1. `LGPL-2.1-only`
    1. `LGPL-2.1-or-later`
    1. `LGPL-2.1+`
    1. `LGPL-3.0`
    1. `LGPL-3.0-only`
    1. `LGPL-3.0-or-later`
    1. `LGPL-3.0+`
    1. `LGPLLR`
    1. `Libpng`
    1. `libpng-2.0`
    1. `libselinux-1.0`
    1. `libtiff`
    1. `LiLiQ-P-1.1`
    1. `LiLiQ-R-1.1`
    1. `LiLiQ-Rplus-1.1`
    1. `Linux-OpenIB`
    1. `LPL-1.0`
    1. `LPL-1.02`
    1. `LPPL-1.0`
    1. `LPPL-1.1`
    1. `LPPL-1.2`
    1. `LPPL-1.3a`
    1. `LPPL-1.3c`
    1. `MakeIndex`
    1. `MirOS`
    1. `MIT`
    1. `MIT-0`
    1. `MIT-advertising`
    1. `MIT-CMU`
    1. `MIT-enna`
    1. `MIT-feh`
    1. `MIT-Modern-Variant`
    1. `MIT-open-group`
    1. `MITNFA`
    1. `Motosoto`
    1. `mpich2`
    1. `MPL-1.0`
    1. `MPL-1.1`
    1. `MPL-2.0`
    1. `MPL-2.0-no-copyleft-exception`
    1. `MS-PL`
    1. `MS-RL`
    1. `MTLL`
    1. `MulanPSL-1.0`
    1. `MulanPSL-2.0`
    1. `Multics`
    1. `Mup`
    1. `NAIST-2003`
    1. `NASA-1.3`
    1. `Naumen`
    1. `NBPL-1.0`
    1. `NCGL-UK-2.0`
    1. `NCSA`
    1. `Net-SNMP`
    1. `NetCDF`
    1. `Newsletr`
    1. `NGPL`
    1. `NIST-PD`
    1. `NIST-PD-fallback`
    1. `NLOD-1.0`
    1. `NLPL`
    1. `Nokia`
    1. `NOSL`
    1. `Noweb`
    1. `NPL-1.0`
    1. `NPL-1.1`
    1. `NPOSL-3.0`
    1. `NRL`
    1. `NTP`
    1. `NTP-0`
    1. `Nunit`
    1. `O-UDA-1.0`
    1. `OCCT-PL`
    1. `OCLC-2.0`
    1. `ODbL-1.0`
    1. `ODC-By-1.0`
    1. `OFL-1.0`
    1. `OFL-1.0-no-RFN`
    1. `OFL-1.0-RFN`
    1. `OFL-1.1`
    1. `OFL-1.1-no-RFN`
    1. `OFL-1.1-RFN`
    1. `OGC-1.0`
    1. `OGDL-Taiwan-1.0`
    1. `OGL-Canada-2.0`
    1. `OGL-UK-1.0`
    1. `OGL-UK-2.0`
    1. `OGL-UK-3.0`
    1. `OGTSL`
    1. `OLDAP-1.1`
    1. `OLDAP-1.2`
    1. `OLDAP-1.3`
    1. `OLDAP-1.4`
    1. `OLDAP-2.0`
    1. `OLDAP-2.0.1`
    1. `OLDAP-2.1`
    1. `OLDAP-2.2`
    1. `OLDAP-2.2.1`
    1. `OLDAP-2.2.2`
    1. `OLDAP-2.3`
    1. `OLDAP-2.4`
    1. `OLDAP-2.5`
    1. `OLDAP-2.6`
    1. `OLDAP-2.7`
    1. `OLDAP-2.8`
    1. `OML`
    1. `OpenSSL`
    1. `OPL-1.0`
    1. `OSET-PL-2.1`
    1. `OSL-1.0`
    1. `OSL-1.1`
    1. `OSL-2.0`
    1. `OSL-2.1`
    1. `OSL-3.0`
    1. `Parity-6.0.0`
    1. `Parity-7.0.0`
    1. `PDDL-1.0`
    1. `PHP-3.0`
    1. `PHP-3.01`
    1. `Plexus`
    1. `PolyForm-Noncommercial-1.0.0`
    1. `PolyForm-Small-Business-1.0.0`
    1. `PostgreSQL`
    1. `PSF-2.0`
    1. `psfrag`
    1. `psutils`
    1. `Python-2.0`
    1. `Qhull`
    1. `QPL-1.0`
    1. `Rdisc`
    1. `RHeCos-1.1`
    1. `RPL-1.1`
    1. `RPL-1.5`
    1. `RPSL-1.0`
    1. `RSA-MD`
    1. `RSCPL`
    1. `Ruby`
    1. `SAX-PD`
    1. `Saxpath`
    1. `SCEA`
    1. `Sendmail`
    1. `Sendmail-8.23`
    1. `SGI-B-1.0`
    1. `SGI-B-1.1`
    1. `SGI-B-2.0`
    1. `SHL-0.5`
    1. `SHL-0.51`
    1. `SimPL-2.0`
    1. `SISSL`
    1. `SISSL-1.2`
    1. `Sleepycat`
    1. `SMLNJ`
    1. `SMPPL`
    1. `SNIA`
    1. `Spencer-86`
    1. `Spencer-94`
    1. `Spencer-99`
    1. `SPL-1.0`
    1. `SSH-OpenSSH`
    1. `SSH-short`
    1. `SSPL-1.0`
    1. `StandardML-NJ`
    1. `SugarCRM-1.1.3`
    1. `SWL`
    1. `TAPR-OHL-1.0`
    1. `TCL`
    1. `TCP-wrappers`
    1. `TMate`
    1. `TORQUE-1.1`
    1. `TOSL`
    1. `TU-Berlin-1.0`
    1. `TU-Berlin-2.0`
    1. `UCL-1.0`
    1. `Unicode-DFS-2015`
    1. `Unicode-DFS-2016`
    1. `Unicode-TOU`
    1. `Unlicense`
    1. `UPL-1.0`
    1. `Vim`
    1. `VOSTROM`
    1. `VSL-1.0`
    1. `W3C`
    1. `W3C-19980720`
    1. `W3C-20150513`
    1. `Watcom-1.0`
    1. `Wsuipa`
    1. `WTFPL`
    1. `wxWindows`
    1. `X11`
    1. `Xerox`
    1. `XFree86-1.1`
    1. `xinetd`
    1. `Xnet`
    1. `xpp`
    1. `XSkat`
    1. `YPL-1.0`
    1. `YPL-1.1`
    1. `Zed`
    1. `Zend-2.0`
    1. `Zimbra-1.3`
    1. `Zimbra-1.4`
    1. `Zlib`
    1. `zlib-acknowledgement`
    1. `ZPL-1.1`
    1. `ZPL-2.0`
    1. `ZPL-2.1`
- required: `false`

SPDX identifier for the license under which a work is made available. The list of identifiers originates from https://raw.githubusercontent.com/spdx/license-list-data/bd8e963a41b13524b2ccb67f9335d2dd397c378e/json/licenses.json.

Usage example:

```yaml
license: Apache-2.0
```
```yaml
license:
  - Apache-2.0
  - MIT
```

### `definitions.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `object`
- required: `false`

...

`definitions.person` has the following properties:

- [`address`](#definitionspersonaddress)
- [`affiliation`](#definitionspersonaffiliation)
- [`alias`](#definitionspersonalias)
- [`city`](#definitionspersoncity)
- [`country`](#definitionspersoncountry)
- [`email`](#definitionspersonemail)
- [`family-names`](#definitionspersonfamily-names)
- [`fax`](#definitionspersonfax)
- [`given-names`](#definitionspersongiven-names)
- [`name-particle`](#definitionspersonname-particle)
- [`name-suffix`](#definitionspersonname-suffix)
- [`orcid`](#definitionspersonorcid)
- [`post-code`](#definitionspersonpost-code)
- [`region`](#definitionspersonregion)
- [`tel`](#definitionspersontel)
- [`website`](#definitionspersonwebsite)


### `definitions.person.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.affiliation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.family-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.given-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.name-particle`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.name-suffix`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.person.website`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.reference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: object
- required: `false`

...

`definitions.reference` has the following properties:

- [`abbreviation`](#definitionsreferenceabbreviation)
- [`abstract`](#definitionsreferenceabstract)
- [`authors`](#definitionsreferenceauthors)
- [`collection-doi`](#definitionsreferencecollection-doi)
- [`collection-title`](#definitionsreferencecollection-title)
- [`collection-type`](#definitionsreferencecollection-type)
- [`commit`](#definitionsreferencecommit)
- [`conference`](#definitionsreferenceconference)
- [`contact`](#definitionsreferencecontact)
- [`copyright`](#definitionsreferencecopyright)
- [`data-type`](#definitionsreferencedata-type)
- [`database-provider`](#definitionsreferencedatabase-provider)
- [`database`](#definitionsreferencedatabase)
- [`date-accessed`](#definitionsreferencedate-accessed)
- [`date-downloaded`](#definitionsreferencedate-downloaded)
- [`date-published`](#definitionsreferencedate-published)
- [`date-released`](#definitionsreferencedate-released)
- [`department`](#definitionsreferencedepartment)
- [`doi`](#definitionsreferencedoi)
- [`edition`](#definitionsreferenceedition)
- [`editors`](#definitionsreferenceeditors)
- [`editors-series`](#definitionsreferenceeditors-series)
- [`end`](#definitionsreferenceend)
- [`entry`](#definitionsreferenceentry)
- [`filename`](#definitionsreferencefilename)
- [`format`](#definitionsreferenceformat)
- [`identifiers`](#definitionsreferenceidentifiers)
- [`institution`](#definitionsreferenceinstitution)
- [`isbn`](#definitionsreferenceisbn)
- [`issn`](#definitionsreferenceissn)
- [`issue`](#definitionsreferenceissue)
- [`issue-date`](#definitionsreferenceissue-date)
- [`issue-title`](#definitionsreferenceissue-title)
- [`journal`](#definitionsreferencejournal)
- [`keywords`](#definitionsreferencekeywords)
- [`languages`](#definitionsreferencelanguages)
- [`license`](#definitionsreferencelicense)
- [`license-url`](#definitionsreferencelicense-url)
- [`loc-end`](#definitionsreferenceloc-end)
- [`loc-start`](#definitionsreferenceloc-start)
- [`location`](#definitionsreferencelocation)
- [`medium`](#definitionsreferencemedium)
- [`month`](#definitionsreferencemonth)
- [`nihmsid`](#definitionsreferencenihmsid)
- [`notes`](#definitionsreferencenotes)
- [`number`](#definitionsreferencenumber)
- [`number-volumes`](#definitionsreferencenumber-volumes)
- [`pages`](#definitionsreferencepages)
- [`patent-states`](#definitionsreferencepatent-states)
- [`pmcid`](#definitionsreferencepmcid)
- [`publisher`](#definitionsreferencepublisher)
- [`recipients`](#definitionsreferencerecipients)
- [`repository`](#definitionsreferencerepository)
- [`repository-artifact`](#definitionsreferencerepository-artifact)
- [`repository-code`](#definitionsreferencerepository-code)
- [`scope`](#definitionsreferencescope)
- [`section`](#definitionsreferencesection)
- [`senders`](#definitionsreferencesenders)
- [`status`](#definitionsreferencestatus)
- [`term`](#definitionsreferenceterm)
- [`thesis-type`](#definitionsreferencethesis-type)
- [`title`](#definitionsreferencetitle)
- [`translators`](#definitionsreferencetranslators)
- [`type`](#definitionsreferencetype)
- [`url`](#definitionsreferenceurl)
- [`version`](#definitionsreferenceversion)
- [`volume`](#definitionsreferencevolume)
- [`volume-title`](#definitionsreferencevolume-title)
- [`year`](#definitionsreferenceyear)
- [`year-original`](#definitionsreferenceyear-original)

### `definitions.reference.abbreviation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  abbreviation: ...
  type: generic
```
```yaml
references:
  - 
    abbreviation: ...
    type: generic
```

### `definitions.reference.abstract`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

The abstract of a work.

- If the work is a journal paper or other academic work: The abstract of the work.
- If the work is a film, broadcast or similar: The synopsis of the work.

Usage examples:

```yaml
preferred-citation:
  abstract: ...
  type: generic
```
```yaml
references:
  - 
    abstract: ...
    type: generic
```

### `definitions.reference.authors`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `true`

...

Usage examples:

```yaml
preferred-citation:
  authors: ...
  type: generic
```
```yaml
references:
  - 
    authors: ...
    type: generic
```

### `definitions.reference.collection-doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  collection-doi: ...
  type: generic
```
```yaml
references:
  - 
    collection-doi: ...
    type: generic
```

### `definitions.reference.collection-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  collection-title: ...
  type: generic
```
```yaml
references:
  - 
    collection-title: ...
    type: generic
```

### `definitions.reference.collection-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  collection-type: ...
  type: generic
```
```yaml
references:
  - 
    collection-type: ...
    type: generic
```

### `definitions.reference.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  commit: ...
  type: generic
```
```yaml
references:
  - 
    commit: ...
    type: generic
```

### `definitions.reference.conference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  conference: ...
  type: generic
```
```yaml
references:
  - 
    conference: ...
    type: generic
```

### `definitions.reference.contact`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
references:
  - 
    contact: ...
    type: generic
```
```yaml
preferred-citation:
  contact: ...
  type: generic
```

### `definitions.reference.copyright`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  copyright: ...
  type: generic
```
```yaml
references:
  - 
    copyright: ...
    type: generic
```

### `definitions.reference.data-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  data-type: ...
  type: generic
```
```yaml
references:
  - 
    data-type: ...
    type: generic
```

### `definitions.reference.database-provider`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  database-provider: ...
  type: generic
```
```yaml
references:
  - 
    database-provider: ...
    type: generic
```

### `definitions.reference.database`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  database: ...
  type: generic
```
```yaml
references:
  - 
    database: ...
    type: generic
```

### `definitions.reference.date-accessed`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  date-accessed: ...
  type: generic
```
```yaml
references:
  - 
    date-accessed: ...
    type: generic
```

### `definitions.reference.date-downloaded`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  date-downloaded: ...
  type: generic
```
```yaml
references:
  - 
    date-downloaded: ...
    type: generic
```

### `definitions.reference.date-published`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
references:
  - 
    date-published: ...
    type: generic
```
```yaml
preferred-citation:
  date-published: ...
  type: generic
```

### `definitions.reference.date-released`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  date-released: ...
  type: generic
```
```yaml
references:
  - 
    date-released: ...
    type: generic
```

### `definitions.reference.department`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  department: ...
  type: generic
```
```yaml
references:
  - 
    department: ...
    type: generic
```

### `definitions.reference.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  doi: ...
  type: generic
```
```yaml
references:
  - 
    doi: ...
    type: generic
```

### `definitions.reference.edition`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  edition: ...
  type: generic
```
```yaml
references:
  - 
    edition: ...
    type: generic
```

### `definitions.reference.editors`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  editors: ...
  type: generic
```
```yaml
references:
  - 
    editors: ...
    type: generic
```

### `definitions.reference.editors-series`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  editors-series: ...
  type: generic
```
```yaml
references:
  - 
    editors-series: ...
    type: generic
```

### `definitions.reference.end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  end: ...
  type: generic
```
```yaml
references:
  - 
    end: ...
    type: generic
```

### `definitions.reference.entry`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  entry: ...
  type: generic
```
```yaml
references:
  - 
    entry: ...
    type: generic
```

### `definitions.reference.filename`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
preferred-citation:
  filename: ...
  type: generic
```
```yaml
references:
  - 
    filename: ...
    type: generic
```

### `definitions.reference.format`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  format: ...
  type: generic
```
```yaml
references:
  - 
    format: ...
    type: generic
```

### `definitions.reference.identifiers`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  identifiers: ...
  type: generic
```
```yaml
references:
  - 
    identifiers: ...
    type: generic
```

### `definitions.reference.institution`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  institution: ...
  type: generic
```
```yaml
references:
  - 
    institution: ...
    type: generic
```

### `definitions.reference.isbn`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  isbn: ...
  type: generic
```
```yaml
references:
  - 
    isbn: ...
    type: generic
```

### `definitions.reference.issn`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  issn: ...
  type: generic
```
```yaml
references:
  - 
    issn: ...
    type: generic
```

### `definitions.reference.issue`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  issue: ...
  type: generic
```
```yaml
references:
  - 
    issue: ...
    type: generic
```

### `definitions.reference.issue-date`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  issue-date: ...
  type: generic
```
```yaml
references:
  - 
    issue-date: ...
    type: generic
```

### `definitions.reference.issue-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  issue-title: ...
  type: generic
```
```yaml
references:
  - 
    issue-title: ...
    type: generic
```

### `definitions.reference.journal`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  journal: ...
  type: generic
```
```yaml
references:
  - 
    journal: ...
    type: generic
```

### `definitions.reference.keywords`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  keywords: ...
  type: generic
```
```yaml
references:
  - 
    keywords: ...
    type: generic
```

### `definitions.reference.languages`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  languages: ...
  type: generic
```
```yaml
references:
  - 
    languages: ...
    type: generic
```

### `definitions.reference.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  license: ...
  type: generic
```
```yaml
references:
  - 
    license: ...
    type: generic
```

### `definitions.reference.license-url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  license-url: ...
  type: generic
```
```yaml
references:
  - 
    license-url: ...
    type: generic
```

### `definitions.reference.loc-end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  loc-end: ...
  type: generic
```
```yaml
references:
  - 
    loc-end: ...
    type: generic
```

### `definitions.reference.loc-start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  loc-start: ...
  type: generic
```
```yaml
references:
  - 
    loc-start: ...
    type: generic
```

### `definitions.reference.location`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  location: ...
  type: generic
```
```yaml
references:
  - 
    location: ...
    type: generic
```

### `definitions.reference.medium`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  medium: ...
  type: generic
```
```yaml
references:
  - 
    medium: ...
    type: generic
```

### `definitions.reference.month`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  month: ...
  type: generic
```
```yaml
references:
  - 
    month: ...
    type: generic
```

### `definitions.reference.nihmsid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  nihmsid: ...
  type: generic
```
```yaml
references:
  - 
    nihmsid: ...
    type: generic
```

### `definitions.reference.notes`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  notes: ...
  type: generic
```
```yaml
references:
  - 
    notes: ...
    type: generic
```

### `definitions.reference.number`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  number: ...
  type: generic
```
```yaml
references:
  - 
    number: ...
    type: generic
```

### `definitions.reference.number-volumes`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  number-volumes: ...
  type: generic
```
```yaml
references:
  - 
    number-volumes: ...
    type: generic
```

### `definitions.reference.pages`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  pages: ...
  type: generic
```
```yaml
references:
  - 
    pages: ...
    type: generic
```

### `definitions.reference.patent-states`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  patent-states: ...
  type: generic
```
```yaml
references:
  - 
    patent-states: ...
    type: generic
```

### `definitions.reference.pmcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
preferred-citation:
  pmcid: ...
  type: generic
```
```yaml
references:
  - 
    pmcid: ...
    type: generic
```

### `definitions.reference.publisher`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  publisher: ...
  type: generic
```
```yaml
references:
  - 
    publisher: ...
    type: generic
```

### `definitions.reference.recipients`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  recipients: ...
  type: generic
```
```yaml
references:
  - 
    recipients: ...
    type: generic
```

### `definitions.reference.repository`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  repository: ...
  type: generic
```
```yaml
references:
  - 
    repository: ...
    type: generic
```

### `definitions.reference.repository-artifact`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  repository-artifact: ...
  type: generic
```
```yaml
references:
  - 
    repository-artifact: ...
    type: generic
```

### `definitions.reference.repository-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  repository-code: ...
  type: generic
```
```yaml
references:
  - 
    repository-code: ...
    type: generic
```

### `definitions.reference.scope`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  scope: ...
  type: generic
```
```yaml
references:
  - 
    scope: ...
    type: generic
```

### `definitions.reference.section`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  section: ...
  type: generic
```
```yaml
references:
  - 
    section: ...
    type: generic
```

### `definitions.reference.senders`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  senders: ...
  type: generic
```
```yaml
references:
  - 
    senders: ...
    type: generic
```

# `definitions.reference.start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  start: ...
  type: generic
```
```yaml
references:
  - 
    start: ...
    type: generic
```

### `definitions.reference.status`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  status: ...
  type: generic
```
```yaml
references:
  - 
    status: ...
    type: generic
```

### `definitions.reference.term`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  term: ...
  type: generic
```
```yaml
references:
  - 
    term: ...
    type: generic
```

### `definitions.reference.thesis-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  thesis-type: ...
  type: generic
```
```yaml
references:
  - 
    thesis-type: ...
    type: generic
```

### `definitions.reference.title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `true`

...

Usage examples:

```yaml
preferred-citation:
  title: ...
  type: generic
```
```yaml
references:
  - 
    title: ...
    type: generic
```

### `definitions.reference.translators`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  translators: ...
  type: generic
```
```yaml
references:
  - 
    translators: ...
    type: generic
```

### `definitions.reference.type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `true`

...

Usage examples:

```yaml
preferred-citation:
    type: generic
```
```yaml
references:
  - 
    type: generic
```

### `definitions.reference.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  type: generic
  url: ...
```
```yaml
references:
  - 
    type: generic
    url: ...
```

### `definitions.reference.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  type: generic
  version: ...
```
```yaml
references:
  - 
    type: generic
    version: ...
```

### `definitions.reference.volume`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  type: generic
  volume: ...
```
```yaml
references:
  - 
    type: generic
    volume: ...
```

### `definitions.reference.volume-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  type: generic
  volume-title: ...
```
```yaml
references:
  - 
    type: generic
    volume-title: ...
```

### `definitions.reference.year`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  type: generic
  year: ...
```
```yaml
references:
  - 
    type: generic
    year: ...
```

### `definitions.reference.year-original`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage examples:

```yaml
preferred-citation:
  type: generic
  year-original: ...
```
```yaml
references:
  - 
    type: generic
    year-original: ...
```

### `definitions.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.swh-identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `...`
- required: `false`

...

Usage example:

```yaml
```

### `definitions.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: `string` or `number`
- required: `false`

...

Usage example:

```yaml
```

