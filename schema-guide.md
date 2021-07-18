# Guide to Citation File Format schema version 1.2.0

## General structure of a CITATION.cff file

TODO

## Glossary of keys

- [`abstract`](#abstract)
- [`authors`](#authors)
- [`cff-version`](#cff-version)
- [`commit`](#commit)
- [`contact`](#contact)
- [`date-released`](#date-released)
- [`definitions`](#definitions)
- [`definitions.address`](#definitions.address)
- [`definitions.alias`](#definitions.alias)
- [`definitions.city`](#definitions.city)
- [`definitions.commit`](#definitions.commit)
- [`definitions.country`](#definitions.country)
- [`definitions.date`](#definitions.date)
- [`definitions.doi`](#definitions.doi)
- [`definitions.email`](#definitions.email)
- [`definitions.entity`](#definitions.entity)
- [`definitions.entity.address`](#definitions.entity.address)
- [`definitions.entity.alias`](#definitions.entity.alias)
- [`definitions.entity.city`](#definitions.entity.city)
- [`definitions.entity.country`](#definitions.entity.country)
- [`definitions.entity.date-end`](#definitions.entity.date-end)
- [`definitions.entity.date-start`](#definitions.entity.date-start)
- [`definitions.entity.email`](#definitions.entity.email)
- [`definitions.entity.fax`](#definitions.entity.fax)
- [`definitions.entity.location`](#definitions.entity.location)
- [`definitions.entity.name`](#definitions.entity.name)
- [`definitions.entity.orcid`](#definitions.entity.orcid)
- [`definitions.entity.post-code`](#definitions.entity.post-code)
- [`definitions.entity.region`](#definitions.entity.region)
- [`definitions.entity.tel`](#definitions.entity.tel)
- [`definitions.entity.type`](#definitions.entity.type)
- [`definitions.entity.website`](#definitions.entity.website)
- [`definitions.fax`](#definitions.fax)
- [`definitions.identifier`](#definitions.identifier)
- [`definitions.identifier-description`](#definitions.identifier-description)
- [`definitions.license`](#definitions.license)
- [`definitions.license-enum`](#definitions.license-enum)
- [`definitions.orcid.description`](#definitions.orcid.description)
- [`definitions.person`](#definitions.person)
- [`definitions.person.address`](#definitions.person.address)
- [`definitions.person.affiliation`](#definitions.person.affiliation)
- [`definitions.person.alias`](#definitions.person.alias)
- [`definitions.person.city`](#definitions.person.city)
- [`definitions.person.country`](#definitions.person.country)
- [`definitions.person.email`](#definitions.person.email)
- [`definitions.person.family-names`](#definitions.person.family-names)
- [`definitions.person.fax`](#definitions.person.fax)
- [`definitions.person.given-names`](#definitions.person.given-names)
- [`definitions.person.name-particle`](#definitions.person.name-particle)
- [`definitions.person.name-suffix`](#definitions.person.name-suffix)
- [`definitions.person.orcid`](#definitions.person.orcid)
- [`definitions.person.post-code`](#definitions.person.post-code)
- [`definitions.person.region`](#definitions.person.region)
- [`definitions.person.tel`](#definitions.person.tel)
- [`definitions.person.website`](#definitions.person.website)
- [`definitions.post-code`](#definitions.post-code)
- [`definitions.reference`](#definitions.reference)
- [`definitions.reference.abbreviation`](#definitions.reference.abbreviation)
- [`definitions.reference.abstract`](#definitions.reference.abstract)
- [`definitions.reference.authors`](#definitions.reference.authors)
- [`definitions.reference.collection-doi`](#definitions.reference.collection-doi)
- [`definitions.reference.collection-title`](#definitions.reference.collection-title)
- [`definitions.reference.collection-type`](#definitions.reference.collection-type)
- [`definitions.reference.commit`](#definitions.reference.commit)
- [`definitions.reference.conference`](#definitions.reference.conference)
- [`definitions.reference.contact`](#definitions.reference.contact)
- [`definitions.reference.copyright`](#definitions.reference.copyright)
- [`definitions.reference.data-type`](#definitions.reference.data-type)
- [`definitions.reference.database-provider`](#definitions.reference.database-provider)
- [`definitions.reference.database.description`](#definitions.reference.database.description)
- [`definitions.reference.date-accessed`](#definitions.reference.date-accessed)
- [`definitions.reference.date-downloaded`](#definitions.reference.date-downloaded)
- [`definitions.reference.date-published`](#definitions.reference.date-published)
- [`definitions.reference.date-released`](#definitions.reference.date-released)
- [`definitions.reference.department`](#definitions.reference.department)
- [`definitions.reference.doi`](#definitions.reference.doi)
- [`definitions.reference.edition`](#definitions.reference.edition)
- [`definitions.reference.editors`](#definitions.reference.editors)
- [`definitions.reference.editors-series`](#definitions.reference.editors-series)
- [`definitions.reference.end`](#definitions.reference.end)
- [`definitions.reference.entry`](#definitions.reference.entry)
- [`definitions.reference.filename`](#definitions.reference.filename)
- [`definitions.reference.format`](#definitions.reference.format)
- [`definitions.reference.identifiers`](#definitions.reference.identifiers)
- [`definitions.reference.institution`](#definitions.reference.institution)
- [`definitions.reference.isbn`](#definitions.reference.isbn)
- [`definitions.reference.issn`](#definitions.reference.issn)
- [`definitions.reference.issue`](#definitions.reference.issue)
- [`definitions.reference.issue-date`](#definitions.reference.issue-date)
- [`definitions.reference.issue-title`](#definitions.reference.issue-title)
- [`definitions.reference.journal`](#definitions.reference.journal)
- [`definitions.reference.keywords`](#definitions.reference.keywords)
- [`definitions.reference.languages`](#definitions.reference.languages)
- [`definitions.reference.license`](#definitions.reference.license)
- [`definitions.reference.license-url`](#definitions.reference.license-url)
- [`definitions.reference.loc-end`](#definitions.reference.loc-end)
- [`definitions.reference.loc-start`](#definitions.reference.loc-start)
- [`definitions.reference.location`](#definitions.reference.location)
- [`definitions.reference.medium`](#definitions.reference.medium)
- [`definitions.reference.month`](#definitions.reference.month)
- [`definitions.reference.nihmsid`](#definitions.reference.nihmsid)
- [`definitions.reference.notes`](#definitions.reference.notes)
- [`definitions.reference.number`](#definitions.reference.number)
- [`definitions.reference.number-volumes`](#definitions.reference.number-volumes)
- [`definitions.reference.pages`](#definitions.reference.pages)
- [`definitions.reference.patent-states`](#definitions.reference.patent-states)
- [`definitions.reference.pmcid`](#definitions.reference.pmcid)
- [`definitions.reference.publisher`](#definitions.reference.publisher)
- [`definitions.reference.recipients`](#definitions.reference.recipients)
- [`definitions.reference.repository`](#definitions.reference.repository)
- [`definitions.reference.repository-artifact`](#definitions.reference.repository-artifact)
- [`definitions.reference.repository-code`](#definitions.reference.repository-code)
- [`definitions.reference.scope`](#definitions.reference.scope)
- [`definitions.reference.section`](#definitions.reference.section)
- [`definitions.reference.senders`](#definitions.reference.senders)
- [`definitions.reference.start`](#definitions.reference.start)
- [`definitions.reference.status`](#definitions.reference.status)
- [`definitions.reference.term`](#definitions.reference.term)
- [`definitions.reference.thesis-type`](#definitions.reference.thesis-type)
- [`definitions.reference.title`](#definitions.reference.title)
- [`definitions.reference.translators`](#definitions.reference.translators)
- [`definitions.reference.type`](#definitions.reference.type)
- [`definitions.reference.type`](#definitions.reference.type)
- [`definitions.reference.url`](#definitions.reference.url)
- [`definitions.reference.version`](#definitions.reference.version)
- [`definitions.reference.volume`](#definitions.reference.volume)
- [`definitions.reference.volume-title`](#definitions.reference.volume-title)
- [`definitions.reference.year`](#definitions.reference.year)
- [`definitions.reference.year-original`](#definitions.reference.year-original)
- [`definitions.region`](#definitions.region)
- [`definitions.swh-identifier`](#definitions.swh-identifier)
- [`definitions.tel`](#definitions.tel)
- [`definitions.url`](#definitions.url)
- [`definitions.version`](#definitions.version)
- [`doi`](#doi)
- [`identifiers`](#identifiers)
- [`keywords`](#keywords)
- [`license`](#license)
- [`license-url`](#license-url)
- [`message`](#message)
- [`preferred-citation`](#preferred-citation)
- [`references`](#references)
- [`repository`](#repository)
- [`repository-artifact`](#repository-artifact)
- [`repository-code`](#repository-code)
- [`title`](#title)
- [`type`](#type)
- [`url`](#url)
- [`version`](#version)


### `abstract`

- **type**: string
- **description**: A description of the software or dataset.

Usage example:

```yaml
abstract: This software implements methods to do things.
```

### `authors`

- **type**: Array of [#definitions.person](#definitions.person) and/or [#definitions.entity](#definitions.entity) objects.
- **description**: The authors of a software or dataset.

Usage example:

```yaml
authors:
  - given-names: Stephan
    family-names: Druskat
  - name: "The Research Software project"
```

### `cff-version`

- **type**: string
- **description**: The Citation File Format schema version that the `CITATION.cff` file adheres to for providing the citation metadata.

Usage example:

```yaml
cff-version: 1.2.0
```

### `commit`

- **type**: string
- **description**: The commit hash or revision number of the software version

Usage example:

```yaml
commit: 1ff847d81f29c45a3a1a5ce73d38e45c2f319bba
```
```yaml
commit: "Revision: 8612"
```

### `contact`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `date-released`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.date`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.date-end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.date-start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.location`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.name`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.entity.website`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.identifier-description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.license-enum`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.orcid.description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.affiliation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.family-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.given-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.name-particle`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.name-suffix`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.person.website`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.abbreviation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.abstract`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

The abstract of a work.

- If the work is a journal paper or other academic work: The abstract of the work.
- If the work is a film, broadcast or similar: The synopsis of the work.

### `definitions.reference.authors`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.collection-doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.collection-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.collection-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.conference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.contact`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.copyright`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.data-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.database-provider`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.database.description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.date-accessed`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.date-downloaded`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.date-published`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.date-released`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.department`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.edition`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.editors`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.editors-series`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.entry`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.filename`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.format`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.identifiers`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.institution`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.isbn`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.issn`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.issue`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.issue-date`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.issue-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.journal`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.keywords`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.languages`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.license-url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.loc-end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.loc-start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.location`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.medium`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.month`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.nihmsid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.notes`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.number`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.number-volumes`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.pages`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.patent-states`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.pmcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.publisher`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.recipients`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.repository`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.repository-artifact`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.repository-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.scope`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.section`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.senders`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.status`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.term`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.thesis-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.translators`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.volume`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.volume-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.year`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.reference.year-original`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.swh-identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `definitions.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- **type**: string or number
- **description**: ...

Usage example:

```yaml
```

### `doi`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `identifiers`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `keywords`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `license`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `license-url`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `message`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `preferred-citation`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `references`

Array of [`#definitions.reference`](#definitions.reference).

### `repository`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `repository-artifact`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `repository-code`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `title`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `type`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `url`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```

### `version`

- **type**: ...
- **description**: ...

Usage example:

```yaml
```
