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

- type: string
- required: false

A description of the software or dataset.

Usage example:

```yaml
abstract: This software implements methods to do things.
```

### `authors`

- type: Array of [definitions.person](#definitionsperson) and/or [definitions.entity](#definitionsentity) objects.
- required: true

The authors of a software or dataset.

Usage example:

```yaml
authors:
  - given-names: Stephan
    family-names: Druskat
  - name: "The Research Software project"
```

### `cff-version`

- type: string
- required: true

The Citation File Format schema version that the `CITATION.cff` file adheres to for providing the citation metadata.

Usage example:

```yaml
cff-version: 1.2.0
```

### `commit`

- type: string
- required: false

The commit hash or revision number of the software version

Usage example:

```yaml
commit: 1ff847d81f29c45a3a1a5ce73d38e45c2f319bba
```
```yaml
commit: "Revision: 8612"
```

### `contact`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `date-released`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `doi`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `identifiers`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `keywords`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `license`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `license-url`

- type: ...
- required: false

...

Usage example:

```yaml
```

### `message`

- type: ...
- default: `"If you use this software, please cite it using the metadata from this file."`
- required: true

...

Usage example:

```yaml
```

### `preferred-citation`

- type: A [`definitions.reference`](#definitionsreference) object. 
- required: false

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

- type: [`definitions.url`](#definitionsurl)
- required: false

The URL of the software or dataset in a repository (when the repository is neither a source code repository nor a build artifact repository).

Usage example:

```yaml
repository: "https://ascl.net/2105.013"
```

### `repository-artifact`

- type: [`definitions.url`](#definitionsurl)
- required: false

The URL of the software in a build artifact/binary repository.

Usage example:

```yaml
repository-artifact: "https://search.maven.org/artifact/org.corpus-tools/cff-maven-plugin/0.4.0/maven-plugin"
```

### `repository-code`

- type: [`definitions.url`](#definitionsurl)
- required: false

The URL of the software in a source code repository.

Usage example:

```yaml
repository-code: "https://github.com/citation-file-format/cff-converter-python"
```

### `title`

- type: string
- required: true

The name of the software or dataset.

Usage example:

```yaml
title: "cffconvert"
```

### `type`

- type: enum (`"software"` or `"dataset"`)
- default: `"software"`
- required: false

The type of the work that is being described by this `CITATION.cff` file.

Usage example:

```yaml
type: "dataset"
```

### `url`

- type: [`definitions.url`](#definitionsurl)
- required: false

The URL of a landing page/website for the software or dataset.

Usage example:

```yaml
url: "https://citation-file-format.github.io/"
```

### `version`

- type: [`definitions.version`](#definitionsversion)
- required: false

The version of the software or dataset.

Usage example:

See [`definitions.version`](#definitionsversion).

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

- type: Nonempty string.
- required: false

An address.


Usage example:

```yaml
```

### `definitions.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- required: false

An alias.

Usage example:

```yaml
```

### `definitions.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- required: false

A city.

Usage example:

```yaml
```

### `definitions.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- required: false

The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.

Usage example:

```yaml
```

### `definitions.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: enum
- required: false

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

- type: string
- required: false

A date.

Usage example:

```yaml
```

### `definitions.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: string
- required: false

The DOI of the work (i.e., `10.5281/zenodo.1003150`, not the resolver URL `http://doi.org/10.5281/zenodo.1003150`).

Usage example:

```yaml
doi: "10.5281/zenodo.1003150"
```

### `definitions.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: string
- required: false

An email address

Usage example:

```yaml
```

### `definitions.entity`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: object
- required: false

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

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.entity.name`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: true

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

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.identifier-description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.license-enum`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: object
- required: false

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

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.affiliation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.family-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.given-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.name-particle`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.name-suffix`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.person.website`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.reference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: object
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: true

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: true

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

- type: ...
- required: false

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

- type: ...
- required: true

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

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

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.swh-identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- required: false

...

Usage example:

```yaml
```

### `definitions.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: string or number
- required: false

The version of a work.

Usage example:

```yaml
version: "1.2.0"
```

```yaml
version: 1.2
```

```yaml
version: "21.10 (Impish Indri)"
```
