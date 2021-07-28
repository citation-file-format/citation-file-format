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
  - family-names: Druskat
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
  - family-names: Druskat
    given-names: Stephan
    orcid: "https://orcid.org/0000-0003-4925-7248"
cff-version: 1.2.0
date-released: "2021-07-18"
identifiers:
  - description: This is the collection of archived snapshots of all versions of My Research Software
    type: doi
    value: "10.5281/zenodo.123456"
  - description: This is the archived snapshot of version 0.11.2 of My Research Software
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
  - family-names: Druskat
    given-names: Stephan
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
title: My Research Software
references:
  authors:
    - family-names: Spaaks
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
  - family-names: Druskat
    given-names: Stephan
cff-version: 1.2.0
message: If you use this software, please cite the article from preferred-citation instead of the software.
title: My Research Software
preferred-citation:
  authors:
    - family-names: Druskat
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

- **type**: Nonempty `string`
- **required**: `false`
- **description**: A description of the software or dataset.
- **usage**:<br><br>
    ```yaml
    abstract: This software implements methods to do things.
    ```

### `authors`

- **type**: Array of [`definitions.person`](#definitionsperson) and/or [`definitions.entity`](#definitionsentity) objects.
- **required**: `true`
- **description**: The authors of a software or dataset.
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

- **type**: Nonempty `string`
- **required**: `true`
- **description**: The Citation File Format schema version that the `CITATION.cff` file adheres to for providing the citation metadata.
- **usage**:<br><br>
    ```yaml
    cff-version: 1.2.0
    ```
    ```yaml
    cff-version: "1.2.0"
    ```

### `commit`

- **type**: Nonempty `string`
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

- **type**: Array of [`definitions.person`](#definitionsperson) and/or [`definitions.entity`](#definitionsentity) objects.
- **required**: `false`
- **description**: The contact person, group, company, etc. for the software or dataset.
- **usage**:<br><br>
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

- **type**: [`definitions.date`](#definitionsdate)
- **required**: `false`
- **description**: The date the software or data set has been released. Format is 4-digit year, 2-digit month, 2-digit day of month, separated by dashes.
- **usage**:<br><br>
    ```yaml
    date-released: 2020-01-31
    ```

### `doi`

- **type**: [`definitions.doi`](#definitionsdoi)
- **required**: `false`
- **description**: The DOI of the software or dataset. This notation is most useful when there is just one DOI you want to include. In
that case, `doi` can be used as shorthand for something like:<br><br>
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
- **usage**:<br><br>
    ```yaml
    doi: 10.5281/zenodo.1003149
    ```
    ```yaml
    doi: 10.5281/zenodo.4813122
    ```

### `identifiers`

- **type**: array of [`definitions.identifier`](#definitionsidentifier) objects.
- **required**: `false`
- **description**: The identifiers of the software or dataset.
- **usage**: see [`definitions.identifier`](#definitionsidentifier).

### `keywords`

- **type**: array of `string`
- **required**: `false`
- **description**: Keywords that describe the work.
- **usage**:<br><br>
    ```yaml
    keywords:
     - thefirstkeyword
     - thesecondkeyword
     - a third keyword
    ```

### `license`

- **type**: (array of) [`definitions.license-enum`](#definitionslicense-enum).
- **required**: `false`
- **description**: The SPDX license identifier(s) for the license(s) under which the work is made available. When there are multiple
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

- **type**: [`definitions.url`](#definitionsurl)
- **required**: `false`
- **description**: The URL of the license text under which the software or dataset is licensed (only for non-standard licenses not included in the SPDX License List).
- **usage**:<br><br>
    ```yaml
    license-url: "https://obscure-licenses.com?id=1234"
    ```

### `message`

- **type**: Nonempty `string`
- **required**: `true`
- **default**: `If you use this software, please cite it using the metadata from this file.`
- **description**: A message to the human reader of the CITATION.cff file to let them know what to do with the citation metadata.
- **usage**:<br><br>
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
    message: If you use this dataset, please cite it using the metadata from this file.
    ```
    ```yaml
    message: Please cite this dataset using these metadata.
    ```
    ```yaml
    message: Please cite this dataset using the metadata from 'preferred-citation'.
    ```

### `preferred-citation`

- **type**: A [`definitions.reference`](#definitionsreference) object.
- **required**: `false`
- **description**: A reference to another work that should be cited instead of the software or dataset itself.  
Note that the principles of [software citation](https://doi.org/10.7717/peerj-cs.86) and [data citation](https://doi.org/10.25490/a97f-egyk) require that 
software should be cited on the same basis as any other research product such as a paper or a book. 
Adding a different preferred citation may result in a violation of the respective
primary principle, "Importance", when others cite this work.
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      authors:
        - family-names: Famnames
          given-names: Given Nam E.
      title: Title of the work.
      type: generic
      year: 2021
    ```

### `references`

- **type**: Array of [`definitions.reference`](#definitionsreference) objects.
- **required**: `false`
- **description**: Reference(s) to other creative works. Similar to a list of references in a paper, references of the software or dataset may include other software (dependencies), or other research products that the software or dataset builds on, but not work describing the software or dataset.
- **usage**: See also [`definitions.reference`](#definitionsreference).<br><br>
    ```yaml
    references:
      - type: software
        authors:
          - name: "The Dependency Project"
        title: "Dependency"
        date-released: 2021-07-26
        doi: 10.5281/zenodo.x1234567
        version: 0.13.4
        repository-code: "https://github.com/dependency-project/dependency"
      - type: article
        scope: Cite this paper if you want to reference the general concepts of the software.
        authors:
          - family-names: Bielefeld
            name-particle: von
            given-names: Arthur
        title: "Towards a 100% accuracy syntax parser for all languages"
        year: 2099
        journal: Journal of Hard Science Fiction
        volume: 42
        issue: 13
        doi: 10.9999/hardscifi-lang.42132
    ```

### `repository`

- **type**: [`definitions.url`](#definitionsurl)
- **required**: false
- **description**: The URL of the software or dataset in a repository (when the repository is neither a source code repository nor a build artifact repository).
- **usage**:<br><br>
    ```yaml
    repository: "https://ascl.net/2105.013"
    ```

### `repository-artifact`

- **type**: [`definitions.url`](#definitionsurl)
- **required**: false
- **description**: The URL of the work in a build artifact/binary repository (when the work is software).
- **usage**:<br><br>
    ```yaml
    repository-artifact: "https://search.maven.org/artifact/org.corpus-tools/cff-maven-plugin/0.4.0/maven-plugin"
    ```

### `repository-code`

- **type**: [`definitions.url`](#definitionsurl)
- **required**: false
- **description**: The URL of the work in a source code repository.
- **usage**:<br><br>
    ```yaml
    repository-code: "https://github.com/citation-file-format/cff-converter-python"
    ```

### `title`

- **type**: Nonempty `string`
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
    type: dataset
    ```

### `url`

- **type**: [`definitions.url`](#definitionsurl)
- **required**: false
- **description**: The URL of a landing page/website for the software or dataset.
- **usage**:<br><br>
    ```yaml
    url: "https://citation-file-format.github.io/"
    ```

### `version`

- **type**: [`definitions.version`](#definitionsversion)
- **required**: `false`
- **description**: The version of the software or dataset.
- **usage**: See [`definitions.version`](#definitionsversion).

## Definitions

Some values in CFF files are valid in different fields.
For example, `repository-code`, `url` and `license-url` all take URLs as values.

The schema therefore has [*definitions*](https://json-schema.org/understanding-json-schema/structuring.html#definitions)
of smaller subschemas, that can be reused in the schema from the respective field, 
instead of having to duplicate them.
For example, there is one definition for a valid URL value ([`definitions.url`](#definitionsurl)),
that is being referenced from `repository-code`, `url` and `license-url`.

**Note:** Definitions are NOT field names, although they may be called similarly.
Do NOT use definitions or subkeys (like `definitions.alias` or `definitions.entity.alias`)
when writing a CFF file.  
To make the definition sections more distinct, their headers are printed in italics, 
such as *`definitions.alias`*.


### Index

- [*`definitions.address`*](#definitionsaddress)
- [*`definitions.alias`*](#definitionsalias)
- [*`definitions.city`*](#definitionscity)
- [*`definitions.commit`*](#definitionscommit)
- [*`definitions.country`*](#definitionscountry)
- [*`definitions.date`*](#definitionsdate)
- [*`definitions.doi`*](#definitionsdoi)
- [*`definitions.email`*](#definitionsemail)
- [*`definitions.entity`*](#definitionsentity) (object)
- [*`definitions.fax`*](#definitionsfax)
- [*`definitions.identifier`*](#definitionsidentifier) (object)
- [*`definitions.identifier-description`*](#definitionsidentifier-description)
- [*`definitions.license`*](#definitionslicense)
- [*`definitions.license-enum`*](#definitionslicense-enum)
- [*`definitions.orcid`*](#definitionsorcid)
- [*`definitions.person`*](#definitionsperson) (object)
- [*`definitions.post-code`*](#definitionspost-code)
- [*`definitions.reference`*](#definitionsreference) (object)
- [*`definitions.region`*](#definitionsregion)
- [*`definitions.swh-identifier`*](#definitionsswh-identifier)
- [*`definitions.tel`*](#definitionstel)
- [*`definitions.url`*](#definitionsurl)
- [*`definitions.version`*](#definitionsversion)

### *`definitions.address`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: An address.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.alias`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: An alias.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.city`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: A city.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.commit`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.country`*

- **type**: `enum`
- **required**: `false`
- **description**: The ISO 3166-1 alpha-2 country code for a country.
- **usage**:<br><br>
    ```yaml
    country: NL
    ```
    ```yaml
    country: DE
    ```

### *`definitions.date`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: A date. Format is 4-digit year, 2-digit month, 2-digit day of month, separated by dashes.
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
      - date-end: "2020-02-02"
        date-start: "2020-01-31"
        type: conference
    ```

Note to tool implementers: it is necessary to cast YAML date objects to string objects when validating against the schema.

### *`definitions.doi`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The DOI of the work (i.e., `10.5281/zenodo.1003150`, not the resolver URL `http://doi.org/10.5281/zenodo.1003150`).
- **usage**:<br><br>
    ```yaml
    doi: "10.5281/zenodo.1003150"
    ```

### *`definitions.email`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: An email address
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.entity`*

- **type**: `object` with the following properties:
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
- **required**: `false`
- **description**: An entity.  
Entities are used in fields that can also take [`definitions.person`](#definitionsperson) objects.
An entity can represent different types of entities, such as a team, an institution, a company, a conference, etc.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: "The Research Software Project team"
    ```

    ```yaml
    contact:
      - name: "The Research Software Project team"
    ```

    ```yaml
    references:
      - type: generic
        title: "A reference showing different fields that take entity objects"
        authors:
          - name: "The Research Software Project team"
        conference:
          - name: "RC21 - Research Conference 2021"
        contact:
          - name: "Customer Support"
        database-provider:
          - name: "Database Provider"
        editors:
          - name: "The Publication Editing Team"
        editors-series:
          - name: "The Publication Series Editing Team"
        institution:
          - name: "Department of Research, Random University"
        location:
          - name: "Museum of Postmodern Art"
        publisher:
          - name: "Open Access Publishing House"
        recipients:
          - name: "The recipient institution of a personal communication"
        senders:
          - name: "The team sending a personal communication"
        translators:
          - name: "Research Translators, Ltd."
    ```

### *`definitions.entity.address`*

- **type**: [`definitions.address`](#definitionsaddress).
- **required**: `false`
- **description**: The entity's address.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        address: "742 Evergreen Terrace"
    ```

### *`definitions.entity.alias`*

- **type**: [`definitions.alias`](#definitionsalias).
- **required**: `false`
- **description**: The entity's alias.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: National Aeronautics and Space Administration
        alias: "NASA"
    ```

### *`definitions.entity.city`*

- **type**: [`definitions.city`](#definitionscity).
- **required**: `false`
- **description**: The entity's city..
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        city: "Berlin"
    ```

### *`definitions.entity.country`*

- **type**: [`definitions.country`](#definitionscountry).
- **required**: `false`
- **description**: The entity's country.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        country: "DE"
    ```

### *`definitions.entity.date-end`*

- **type**: [`definitions.date`](#definitionsdate).
- **required**: `false`
- **description**: The entity's ending date, e.g. when the entity is a conference.
- **usage**:<br><br>
    ```yaml
    references:
      - type: conference-paper
        title: "Conference Paper"
        authors:
          - name: The Research Software Project
        conference:
          - name: "Research Conference 2021"
            date-end: 2021-07-27
    ```

### *`definitions.entity.date-start`*

- **type**: [`definitions.date`](#definitionsdate).
- **required**: `false`
- **description**: The entity's starting date, e.g. when the entity is a conference.
- **usage**:<br><br>
    ```yaml
    references:
      - type: conference-paper
        title: "Conference Paper"
        authors:
          - name: The Research Software Project
        conference:
          - name: "Research Conference 2021"
            date-start: 2021-07-27
    ```

### *`definitions.entity.email`*

- **type**: [`definitions.email`](#definitionsemail).
- **required**: `false`
- **description**: The entity's email address.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        email: "team@research-software.org"
    ```

### *`definitions.entity.fax`*

- **type**: [`definitions.fax`](#definitionsfax).
- **required**: `false`
- **description**: The entity's fax number.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        fax: +12-3456-7890
    ```

### *`definitions.entity.location`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The entity's location.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        location: "Lovelace Building, room 0.42"
    ```

### *`definitions.entity.name`*

- **type**: Nonempty `string`
- **required**: `true`
- **description**: The entity's name.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
    ```

### *`definitions.entity.orcid`*

- **type**: [`definitions.orcid`](#definitionsorcid).
- **required**: `false`
- **description**: The entity's orcid.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        orcid: "https://orcid.org/0000-0003-4925-7248"
    ```

### *`definitions.entity.post-code`*

- **type**: [`definitions.post-code`](#definitionspost-code).
- **required**: `false`
- **description**: The entity's post code.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        post-code: 90210
    ```

    ```yaml
    authors:
      - name: The Research Software Project
        post-code: "90210"
    ```

### *`definitions.entity.region`*

- **type**: [`definitions.region`](#definitionsregion).
- **required**: `false`
- **description**: The entity's region.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        region: "Renfrewshire"
    ```

### *`definitions.entity.tel`*

- **type**: [`definitions.tel`](#definitionstel).
- **required**: `false`
- **description**: The entity's telephone number.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        tel: +12-345-6789098
    ```

### *`definitions.entity.website`*

- **type**: [`definitions.url`](#definitionsurl).
- **required**: `false`
- **description**: The entity's website.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        website: https://research-software-project.org
    ```

### *`definitions.fax`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: A fax number.
- **usage**:<br><br>
    ```yaml
    authors:
      - name: The Research Software Project
        fax: +12-3456-7890
    ```
    ```yaml
    authors:
      - family-names: McClane
        fax: +12-3456-7890
        given-names: John
    ```

### *`definitions.identifier`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
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
        description: The GitHub release URL of tag 1.1.0.
      - type: url
        value: https://github.com/citation-file-format/citation-file-format/tree/16192bf05e99bcb35d5c3e085047807b5720fafc
        description: The GitHub release URL of the commit tagged with 1.1.0.
    ```

### *`definitions.identifier-description`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.license`*

- **type**: (array of) [`definitions.license-enum`](#definitions.license-enum) objects.
- **required**: `false`
- **description**: License identifier(s) under which the work is made available. When there are multiple licenses, it is assumed their relationship is OR, not AND.
- **usage**:<br><br>
    ```yaml
    license: Apache-2.0
    ```
    ```yaml
    license:
      - Apache-2.0
      - MIT
    ```

### *`definitions.license-enum`*

- **type**: `enum` with values:
    - `0BSD`
    - `AAL`
    - `Abstyles`
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
    - `APSL-1.0`
    - `APSL-1.1`
    - `APSL-1.2`
    - `APSL-2.0`
    - `Artistic-1.0`
    - `Artistic-1.0-cl8`
    - `Artistic-1.0-Perl`
    - `Artistic-2.0`
    - `Bahyph`
    - `Barr`
    - `Beerware`
    - `BitTorrent-1.0`
    - `BitTorrent-1.1`
    - `blessing`
    - `BlueOak-1.0.0`
    - `Borceux`
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
    - `BSD-3-Clause-No-Nuclear-License`
    - `BSD-3-Clause-No-Nuclear-License-2014`
    - `BSD-3-Clause-No-Nuclear-Warranty`
    - `BSD-3-Clause-Open-MPI`
    - `BSD-4-Clause`
    - `BSD-4-Clause-Shortened`
    - `BSD-4-Clause-UC`
    - `BSD-Protection`
    - `BSD-Source-Code`
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
    - `CC-BY-3.0`
    - `CC-BY-3.0-AT`
    - `CC-BY-3.0-US`
    - `CC-BY-4.0`
    - `CC-BY-NC-1.0`
    - `CC-BY-NC-2.0`
    - `CC-BY-NC-2.5`
    - `CC-BY-NC-3.0`
    - `CC-BY-NC-4.0`
    - `CC-BY-NC-ND-1.0`
    - `CC-BY-NC-ND-2.0`
    - `CC-BY-NC-ND-2.5`
    - `CC-BY-NC-ND-3.0`
    - `CC-BY-NC-ND-3.0-IGO`
    - `CC-BY-NC-ND-4.0`
    - `CC-BY-NC-SA-1.0`
    - `CC-BY-NC-SA-2.0`
    - `CC-BY-NC-SA-2.5`
    - `CC-BY-NC-SA-3.0`
    - `CC-BY-NC-SA-4.0`
    - `CC-BY-ND-1.0`
    - `CC-BY-ND-2.0`
    - `CC-BY-ND-2.5`
    - `CC-BY-ND-3.0`
    - `CC-BY-ND-4.0`
    - `CC-BY-SA-1.0`
    - `CC-BY-SA-2.0`
    - `CC-BY-SA-2.0-UK`
    - `CC-BY-SA-2.1-JP`
    - `CC-BY-SA-2.5`
    - `CC-BY-SA-3.0`
    - `CC-BY-SA-3.0-AT`
    - `CC-BY-SA-4.0`
    - `CC-PDDC`
    - `CC0-1.0`
    - `CDDL-1.0`
    - `CDDL-1.1`
    - `CDL-1.0`
    - `CDLA-Permissive-1.0`
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
    - `ClArtistic`
    - `CNRI-Jython`
    - `CNRI-Python`
    - `CNRI-Python-GPL-Compatible`
    - `Condor-1.1`
    - `copyleft-next-0.3.0`
    - `copyleft-next-0.3.1`
    - `CPAL-1.0`
    - `CPL-1.0`
    - `CPOL-1.02`
    - `Crossword`
    - `CrystalStacker`
    - `CUA-OPL-1.0`
    - `Cube`
    - `curl`
    - `D-FSL-1.0`
    - `diffmark`
    - `DOC`
    - `Dotseqn`
    - `DRL-1.0`
    - `DSDP`
    - `dvipdfm`
    - `ECL-1.0`
    - `ECL-2.0`
    - `eCos-2.0`
    - `EFL-1.0`
    - `EFL-2.0`
    - `eGenix`
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
    - `Frameworx-1.0`
    - `FreeBSD-DOC`
    - `FreeImage`
    - `FSFAP`
    - `FSFUL`
    - `FSFULLR`
    - `FTL`
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
    - `gSOAP-1.3b`
    - `HaskellReport`
    - `Hippocratic-2.1`
    - `HPND`
    - `HPND-sell-variant`
    - `HTMLTIDY`
    - `IBM-pibs`
    - `ICU`
    - `IJG`
    - `ImageMagick`
    - `iMatix`
    - `Imlib2`
    - `Info-ZIP`
    - `Intel`
    - `Intel-ACPI`
    - `Interbase-1.0`
    - `IPA`
    - `IPL-1.0`
    - `ISC`
    - `JasPer-2.0`
    - `JPNIC`
    - `JSON`
    - `LAL-1.2`
    - `LAL-1.3`
    - `Latex2e`
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
    - `LiLiQ-P-1.1`
    - `LiLiQ-R-1.1`
    - `LiLiQ-Rplus-1.1`
    - `Linux-OpenIB`
    - `LPL-1.0`
    - `LPL-1.02`
    - `LPPL-1.0`
    - `LPPL-1.1`
    - `LPPL-1.2`
    - `LPPL-1.3a`
    - `LPPL-1.3c`
    - `MakeIndex`
    - `MirOS`
    - `MIT`
    - `MIT-0`
    - `MIT-advertising`
    - `MIT-CMU`
    - `MIT-enna`
    - `MIT-feh`
    - `MIT-Modern-Variant`
    - `MIT-open-group`
    - `MITNFA`
    - `Motosoto`
    - `mpich2`
    - `MPL-1.0`
    - `MPL-1.1`
    - `MPL-2.0`
    - `MPL-2.0-no-copyleft-exception`
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
    - `NIST-PD`
    - `NIST-PD-fallback`
    - `NLOD-1.0`
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
    - `OML`
    - `OpenSSL`
    - `OPL-1.0`
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
    - `PolyForm-Noncommercial-1.0.0`
    - `PolyForm-Small-Business-1.0.0`
    - `PostgreSQL`
    - `PSF-2.0`
    - `psfrag`
    - `psutils`
    - `Python-2.0`
    - `Qhull`
    - `QPL-1.0`
    - `Rdisc`
    - `RHeCos-1.1`
    - `RPL-1.1`
    - `RPL-1.5`
    - `RPSL-1.0`
    - `RSA-MD`
    - `RSCPL`
    - `Ruby`
    - `SAX-PD`
    - `Saxpath`
    - `SCEA`
    - `Sendmail`
    - `Sendmail-8.23`
    - `SGI-B-1.0`
    - `SGI-B-1.1`
    - `SGI-B-2.0`
    - `SHL-0.5`
    - `SHL-0.51`
    - `SimPL-2.0`
    - `SISSL`
    - `SISSL-1.2`
    - `Sleepycat`
    - `SMLNJ`
    - `SMPPL`
    - `SNIA`
    - `Spencer-86`
    - `Spencer-94`
    - `Spencer-99`
    - `SPL-1.0`
    - `SSH-OpenSSH`
    - `SSH-short`
    - `SSPL-1.0`
    - `StandardML-NJ`
    - `SugarCRM-1.1.3`
    - `SWL`
    - `TAPR-OHL-1.0`
    - `TCL`
    - `TCP-wrappers`
    - `TMate`
    - `TORQUE-1.1`
    - `TOSL`
    - `TU-Berlin-1.0`
    - `TU-Berlin-2.0`
    - `UCL-1.0`
    - `Unicode-DFS-2015`
    - `Unicode-DFS-2016`
    - `Unicode-TOU`
    - `Unlicense`
    - `UPL-1.0`
    - `Vim`
    - `VOSTROM`
    - `VSL-1.0`
    - `W3C`
    - `W3C-19980720`
    - `W3C-20150513`
    - `Watcom-1.0`
    - `Wsuipa`
    - `WTFPL`
    - `wxWindows`
    - `X11`
    - `Xerox`
    - `XFree86-1.1`
    - `xinetd`
    - `Xnet`
    - `xpp`
    - `XSkat`
    - `YPL-1.0`
    - `YPL-1.1`
    - `Zed`
    - `Zend-2.0`
    - `Zimbra-1.3`
    - `Zimbra-1.4`
    - `Zlib`
    - `zlib-acknowledgement`
    - `ZPL-1.1`
    - `ZPL-2.0`
    - `ZPL-2.1`
- **required**: `false`
- **description**: SPDX identifier for the license under which a work is made available. The list of identifiers originates from https://github.com/spdx/license-list-data/blob/bd8e963a41b13524b2ccb67f9335d2dd397c378e/json/licenses.json.
- **usage**:<br><br>
    ```yaml
    license: Apache-2.0
    ```
    ```yaml
    license:
      - Apache-2.0
      - MIT
    ```

### *`definitions.orcid`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person`*

- **type**: `object` with the following properties:
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
- **required**: `false`
- **description**: A person.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.address`*

- **type**: [`definitions.address`](#definitionsaddress)
- **required**: `false`
- **description**: The person's address.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.affiliation`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The person's affiliation.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.alias`*

- **type**: [`definitions.alias`](#definitionsalias)
- **required**: `false`
- **description**: The person's alias.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.city`*

- **type**: [`definitions.city`](#definitionscity)
- **required**: `false`
- **description**: The person's city.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.country`*

- **type**: [`definitions.country`](#definitioncountry)
- **required**: `false`
- **description**: The person's country.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.email`*

- **type**: [`definitions.email`](#definitionsemail)
- **required**: `false`
- **description**: The person's email address.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.family-names`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The person's family names.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.fax`*

- **type**: [`definitions.fax`](#definitionsfax)
- **required**: `false`
- **description**: The person's fax number.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: McClane
        fax: +12-3456-7890
        given-names: John
    ```

### *`definitions.person.given-names`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The person's given names.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.name-particle`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The person's name particle, e.g., a nobiliary particle or a preposition meaning 'of' or 'from' (for example 'von' in 'Alexander von Humboldt').
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.name-suffix`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The person's name-suffix, e.g. 'Jr.' for Sammy Davis Jr. or 'III' for Frank Edwin Wright III.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.orcid`*

- **type**: [`definitions.orcid`](#definitionsorcid)
- **required**: `false`
- **description**: The person's [ORCID](https://orcid.org) identifier.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.post-code`*

- **type**: [`definitions.post-code`](#definitionspost-code)
- **required**: `false`
- **description**: The person's post code.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.region`*

- **type**: [`definitions.region`](#definitionsregion)
- **required**: `false`
- **description**: The person's region.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.person.tel`*

- **type**: [`definitions.tel`](#definitionstel)
- **required**: `false`
- **description**: The person's telephone number.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: McClane
        given-names: John
        tel: +12-345-6789098
    ```

### *`definitions.person.website`*

- **type**: [`definitions.url`](#definitionsurl)
- **required**: `false`
- **description**: The person's website.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: Druskat
        given-names: Stephan
        website: https://sdruskat.net
    ```

### *`definitions.post-code`*

- **type**: `...`
- **required**: `false`
- **description**: A post code.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.reference`*

- **type**: `object` with the following properties:
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
- **required**: `false`
- **description**: A reference.
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.reference.abbreviation`*

- **type**: Nonempty `string`
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
      - 
        abbreviation: DEF
        type: generic
    ```

### *`definitions.reference.abstract`*

- **type**: `...`
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
      - 
        abstract: "This work implements an algorithm that we use in our software. etc."
        type: generic
    ```

### *`definitions.reference.authors`*

- **type**: `...`
- **required**: `true`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      authors: ...
      type: generic
    ```
    ```yaml
    references:
      - authors: ...
        type: generic
    ```

### *`definitions.reference.collection-doi`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      collection-doi: ...
      type: generic
    ```
    ```yaml
    references:
      - collection-doi: ...
        type: generic
    ```

### *`definitions.reference.collection-title`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      collection-title: ...
      type: generic
    ```
    ```yaml
    references:
      - collection-title: ...
        type: generic
    ```

### *`definitions.reference.collection-type`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      collection-type: ...
      type: generic
    ```
    ```yaml
    references:
      - collection-type: ...
        type: generic
    ```

### *`definitions.reference.commit`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      commit: ...
      type: generic
    ```
    ```yaml
    references:
      - commit: ...
        type: generic
    ```

### *`definitions.reference.conference`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      conference: ...
      type: generic
    ```
    ```yaml
    references:
      - conference: ...
        type: generic
    ```

### *`definitions.reference.contact`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    references:
      - contact: ...
        type: generic
    ```
    ```yaml
    preferred-citation:
      contact: ...
      type: generic
    ```

### *`definitions.reference.copyright`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      copyright: ...
      type: generic
    ```
    ```yaml
    references:
      - copyright: ...
        type: generic
    ```

### *`definitions.reference.data-type`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      data-type: ...
      type: generic
    ```
    ```yaml
    references:
      - data-type: ...
        type: generic
    ```

### *`definitions.reference.database-provider`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      database-provider: ...
      type: generic
    ```
    ```yaml
    references:
      - database-provider: ...
        type: generic
    ```

### *`definitions.reference.database`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      database: ...
      type: generic
    ```
    ```yaml
    references:
      - database: ...
        type: generic
    ```

### *`definitions.reference.date-accessed`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      date-accessed: ...
      type: generic
    ```
    ```yaml
    references:
      - date-accessed: ...
        type: generic
    ```

### *`definitions.reference.date-downloaded`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      date-downloaded: ...
      type: generic
    ```
    ```yaml
    references:
      - date-downloaded: ...
        type: generic
    ```

### *`definitions.reference.date-published`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    references:
      - date-published: ...
        type: generic
    ```
    ```yaml
    preferred-citation:
      date-published: ...
      type: generic
    ```

### *`definitions.reference.date-released`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      date-released: ...
      type: generic
    ```
    ```yaml
    references:
      - date-released: ...
        type: generic
    ```

### *`definitions.reference.department`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      department: ...
      type: generic
    ```
    ```yaml
    references:
      - department: ...
        type: generic
    ```

### *`definitions.reference.doi`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      doi: ...
      type: generic
    ```
    ```yaml
    references:
      - doi: ...
        type: generic
    ```

### *`definitions.reference.edition`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      edition: ...
      type: generic
    ```
    ```yaml
    references:
      - edition: ...
        type: generic
    ```

### *`definitions.reference.editors`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      editors: ...
      type: generic
    ```
    ```yaml
    references:
      - editors: ...
        type: generic
    ```

### *`definitions.reference.editors-series`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      editors-series: ...
      type: generic
    ```
    ```yaml
    references:
      - editors-series: ...
        type: generic
    ```

### *`definitions.reference.end`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      end: ...
      type: generic
    ```
    ```yaml
    references:
      - end: ...
        type: generic
    ```

### *`definitions.reference.entry`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      entry: ...
      type: generic
    ```
    ```yaml
    references:
      - entry: ...
        type: generic
    ```

### *`definitions.reference.filename`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      filename: ...
      type: generic
    ```
    ```yaml
    references:
      - filename: ...
        type: generic
    ```

### *`definitions.reference.format`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      format: ...
      type: generic
    ```
    ```yaml
    references:
      - format: ...
        type: generic
    ```

### *`definitions.reference.identifiers`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      identifiers: ...
      type: generic
    ```
    ```yaml
    references:
      - identifiers: ...
        type: generic
    ```

### *`definitions.reference.institution`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      institution: ...
      type: generic
    ```
    ```yaml
    references:
      - institution: ...
        type: generic
    ```

### *`definitions.reference.isbn`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      isbn: ...
      type: generic
    ```
    ```yaml
    references:
      - isbn: ...
        type: generic
    ```

### *`definitions.reference.issn`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issn: ...
      type: generic
    ```
    ```yaml
    references:
      - issn: ...
        type: generic
    ```

### *`definitions.reference.issue`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issue: ...
      type: generic
    ```
    ```yaml
    references:
      - issue: ...
        type: generic
    ```

### *`definitions.reference.issue-date`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issue-date: ...
      type: generic
    ```
    ```yaml
    references:
      - issue-date: ...
        type: generic
    ```

### *`definitions.reference.issue-title`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      issue-title: ...
      type: generic
    ```
    ```yaml
    references:
      - issue-title: ...
        type: generic
    ```

### *`definitions.reference.journal`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      journal: ...
      type: generic
    ```
    ```yaml
    references:
      - journal: ...
        type: generic
    ```

### *`definitions.reference.keywords`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      keywords: ...
      type: generic
    ```
    ```yaml
    references:
      - keywords: ...
        type: generic
    ```

### *`definitions.reference.languages`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      languages: ...
      type: generic
    ```
    ```yaml
    references:
      - languages: ...
        type: generic
    ```

### *`definitions.reference.license`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      license: ...
      type: generic
    ```
    ```yaml
    references:
      - license: ...
        type: generic
    ```

### *`definitions.reference.license-url`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      license-url: ...
      type: generic
    ```
    ```yaml
    references:
      - license-url: ...
        type: generic
    ```

### *`definitions.reference.loc-end`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      loc-end: ...
      type: generic
    ```
    ```yaml
    references:
      - loc-end: ...
        type: generic
    ```

### *`definitions.reference.loc-start`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      loc-start: ...
      type: generic
    ```
    ```yaml
    references:
      - loc-start: ...
        type: generic
    ```

### *`definitions.reference.location`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      location: ...
      type: generic
    ```
    ```yaml
    references:
      - location: ...
        type: generic
    ```

### *`definitions.reference.medium`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      medium: ...
      type: generic
    ```
    ```yaml
    references:
      - medium: ...
        type: generic
    ```

### *`definitions.reference.month`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      month: ...
      type: generic
    ```
    ```yaml
    references:
      - month: ...
        type: generic
    ```

### *`definitions.reference.nihmsid`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      nihmsid: ...
      type: generic
    ```
    ```yaml
    references:
      - nihmsid: ...
        type: generic
    ```

### *`definitions.reference.notes`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      notes: ...
      type: generic
    ```
    ```yaml
    references:
      - notes: ...
        type: generic
    ```

### *`definitions.reference.number`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      number: ...
      type: generic
    ```
    ```yaml
    references:
      - number: ...
        type: generic
    ```

### *`definitions.reference.number-volumes`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      number-volumes: ...
      type: generic
    ```
    ```yaml
    references:
      - number-volumes: ...
        type: generic
    ```

### *`definitions.reference.pages`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      pages: ...
      type: generic
    ```
    ```yaml
    references:
      - pages: ...
        type: generic
    ```

### *`definitions.reference.patent-states`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      patent-states: ...
      type: generic
    ```
    ```yaml
    references:
      - patent-states: ...
        type: generic
    ```

### *`definitions.reference.pmcid`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      pmcid: ...
      type: generic
    ```
    ```yaml
    references:
      - pmcid: ...
        type: generic
    ```

### *`definitions.reference.publisher`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      publisher: ...
      type: generic
    ```
    ```yaml
    references:
      - publisher: ...
        type: generic
    ```

### *`definitions.reference.recipients`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      recipients: ...
      type: generic
    ```
    ```yaml
    references:
      - recipients: ...
        type: generic
    ```

### *`definitions.reference.repository`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      repository: ...
      type: generic
    ```
    ```yaml
    references:
      - repository: ...
        type: generic
    ```

### *`definitions.reference.repository-artifact`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      repository-artifact: ...
      type: generic
    ```
    ```yaml
    references:
      - repository-artifact: ...
        type: generic
    ```

### *`definitions.reference.repository-code`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      repository-code: ...
      type: generic
    ```
    ```yaml
    references:
      - repository-code: ...
        type: generic
    ```

### *`definitions.reference.scope`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      scope: ...
      type: generic
    ```
    ```yaml
    references:
      - scope: ...
        type: generic
    ```

### *`definitions.reference.section`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      section: ...
      type: generic
    ```
    ```yaml
    references:
      - section: ...
        type: generic
    ```

### *`definitions.reference.senders`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      senders: ...
      type: generic
    ```
    ```yaml
    references:
      - senders: ...
        type: generic
    ```

### *`definitions.reference.start`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      start: ...
      type: generic
    ```
    ```yaml
    references:
      - start: ...
        type: generic
    ```

### *`definitions.reference.status`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      status: ...
      type: generic
    ```
    ```yaml
    references:
      - status: ...
        type: generic
    ```

### *`definitions.reference.term`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      term: ...
      type: generic
    ```
    ```yaml
    references:
      - term: ...
        type: generic
    ```

### *`definitions.reference.thesis-type`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      thesis-type: ...
      type: generic
    ```
    ```yaml
    references:
      - thesis-type: ...
        type: generic
    ```

### *`definitions.reference.title`*

- **type**: `...`
- **required**: `true`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      title: ...
      type: generic
    ```
    ```yaml
    references:
      - title: ...
        type: generic
    ```

### *`definitions.reference.translators`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      translators: ...
      type: generic
    ```
    ```yaml
    references:
      - translators: ...
        type: generic
    ```

### *`definitions.reference.type`*

- **type**: `...`
- **required**: `true`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
        type: generic
    ```
    ```yaml
    references:
      - type: generic
    ```

### *`definitions.reference.url`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      url: ...
    ```
    ```yaml
    references:
      - type: generic
        url: ...
    ```

### *`definitions.reference.version`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      version: ...
    ```
    ```yaml
    references:
      - type: generic
        version: ...
    ```

### *`definitions.reference.volume`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      volume: ...
    ```
    ```yaml
    references:
      - type: generic
        volume: ...
    ```

### *`definitions.reference.volume-title`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      volume-title: ...
    ```
    ```yaml
    references:
      - type: generic
        volume-title: ...
    ```

### *`definitions.reference.year`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      year: ...
    ```
    ```yaml
    references:
      - type: generic
        year: ...
    ```

### *`definitions.reference.year-original`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    preferred-citation:
      type: generic
      year-original: ...
    ```
    ```yaml
    references:
      - type: generic
        year-original: ...
    ```

### *`definitions.region`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.swh-identifier`*

- **type**: `...`
- **required**: `false`
- **description**: ...
- **usage**:<br><br>
    ```yaml
    ```

### *`definitions.tel`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: A telephone number.
- **usage**:<br><br>
    ```yaml
    authors:
      - family-names: McClane
        given-names: John
        tel: +12-345-6789098
    ```
    ```yaml
    authors:
      - name: The Research Software Project
        tel: +12-345-6789098
    ```

### *`definitions.url`*

- **type**: Nonempty `string`
- **required**: `false`
- **description**: The URL of a landing page/website for the software or dataset. Supported URLs start with one of:
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
      - name: The Research Software Project
        url: "https://research-software-project.org"
    ```
    ```yaml
    references:
      - name: The Research Software Project
        url: "sftp://files.research-software-project.org"
    ```


### *`definitions.version`*

- **type**: Nonempty `string` or `number`
- **required**: `false`
- **description**: The version of a work.
- **usage**: 
    ```yaml
    version: "1.2.0"
    ```
    ```yaml
    version: 1.2
    ```
    ```yaml
    version: "21.10 (Impish Indri)"
    ```
