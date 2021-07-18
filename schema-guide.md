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
- [`definitions.address`](#definitionsaddress)
- [`definitions.alias`](#definitionsalias)
- [`definitions.city`](#definitionscity)
- [`definitions.commit`](#definitionscommit)
- [`definitions.country`](#definitionscountry)
- [`definitions.date`](#definitionsdate)
- [`definitions.doi`](#definitionsdoi)
- [`definitions.email`](#definitionsemail)
- [`definitions.entity`](#definitionsentity)
- [`definitions.entity.address`](#definitionsentityaddress)
- [`definitions.entity.alias`](#definitionsentityalias)
- [`definitions.entity.city`](#definitionsentitycity)
- [`definitions.entity.country`](#definitionsentitycountry)
- [`definitions.entity.date-end`](#definitionsentitydate-end)
- [`definitions.entity.date-start`](#definitionsentitydate-start)
- [`definitions.entity.email`](#definitionsentityemail)
- [`definitions.entity.fax`](#definitionsentityfax)
- [`definitions.entity.location`](#definitionsentitylocation)
- [`definitions.entity.name`](#definitionsentityname)
- [`definitions.entity.orcid`](#definitionsentityorcid)
- [`definitions.entity.post-code`](#definitionsentitypost-code)
- [`definitions.entity.region`](#definitionsentityregion)
- [`definitions.entity.tel`](#definitionsentitytel)
- [`definitions.entity.website`](#definitionsentitywebsite)
- [`definitions.fax`](#definitionsfax)
- [`definitions.identifier`](#definitionsidentifier)
- [`definitions.identifier-description`](#definitionsidentifier-description)
- [`definitions.license`](#definitionslicense)
- [`definitions.license-enum`](#definitionslicense-enum)
- [`definitions.orcid.description`](#definitionsorciddescription)
- [`definitions.person`](#definitionsperson)
- [`definitions.person.address`](#definitionspersonaddress)
- [`definitions.person.affiliation`](#definitionspersonaffiliation)
- [`definitions.person.alias`](#definitionspersonalias)
- [`definitions.person.city`](#definitionspersoncity)
- [`definitions.person.country`](#definitionspersoncountry)
- [`definitions.person.email`](#definitionspersonemail)
- [`definitions.person.family-names`](#definitionspersonfamily-names)
- [`definitions.person.fax`](#definitionspersonfax)
- [`definitions.person.given-names`](#definitionspersongiven-names)
- [`definitions.person.name-particle`](#definitionspersonname-particle)
- [`definitions.person.name-suffix`](#definitionspersonname-suffix)
- [`definitions.person.orcid`](#definitionspersonorcid)
- [`definitions.person.post-code`](#definitionspersonpost-code)
- [`definitions.person.region`](#definitionspersonregion)
- [`definitions.person.tel`](#definitionspersontel)
- [`definitions.person.website`](#definitionspersonwebsite)
- [`definitions.post-code`](#definitionspost-code)
- [`definitions.reference`](#definitionsreference)
- [`definitions.reference.abbreviation`](#definitionsreferenceabbreviation)
- [`definitions.reference.abstract`](#definitionsreferenceabstract)
- [`definitions.reference.authors`](#definitionsreferenceauthors)
- [`definitions.reference.collection-doi`](#definitionsreferencecollection-doi)
- [`definitions.reference.collection-title`](#definitionsreferencecollection-title)
- [`definitions.reference.collection-type`](#definitionsreferencecollection-type)
- [`definitions.reference.commit`](#definitionsreferencecommit)
- [`definitions.reference.conference`](#definitionsreferenceconference)
- [`definitions.reference.contact`](#definitionsreferencecontact)
- [`definitions.reference.copyright`](#definitionsreferencecopyright)
- [`definitions.reference.data-type`](#definitionsreferencedata-type)
- [`definitions.reference.database-provider`](#definitionsreferencedatabase-provider)
- [`definitions.reference.database`](#definitionsreferencedatabase)
- [`definitions.reference.date-accessed`](#definitionsreferencedate-accessed)
- [`definitions.reference.date-downloaded`](#definitionsreferencedate-downloaded)
- [`definitions.reference.date-published`](#definitionsreferencedate-published)
- [`definitions.reference.date-released`](#definitionsreferencedate-released)
- [`definitions.reference.department`](#definitionsreferencedepartment)
- [`definitions.reference.doi`](#definitionsreferencedoi)
- [`definitions.reference.edition`](#definitionsreferenceedition)
- [`definitions.reference.editors`](#definitionsreferenceeditors)
- [`definitions.reference.editors-series`](#definitionsreferenceeditors-series)
- [`definitions.reference.end`](#definitionsreferenceend)
- [`definitions.reference.entry`](#definitionsreferenceentry)
- [`definitions.reference.filename`](#definitionsreferencefilename)
- [`definitions.reference.format`](#definitionsreferenceformat)
- [`definitions.reference.identifiers`](#definitionsreferenceidentifiers)
- [`definitions.reference.institution`](#definitionsreferenceinstitution)
- [`definitions.reference.isbn`](#definitionsreferenceisbn)
- [`definitions.reference.issn`](#definitionsreferenceissn)
- [`definitions.reference.issue`](#definitionsreferenceissue)
- [`definitions.reference.issue-date`](#definitionsreferenceissue-date)
- [`definitions.reference.issue-title`](#definitionsreferenceissue-title)
- [`definitions.reference.journal`](#definitionsreferencejournal)
- [`definitions.reference.keywords`](#definitionsreferencekeywords)
- [`definitions.reference.languages`](#definitionsreferencelanguages)
- [`definitions.reference.license`](#definitionsreferencelicense)
- [`definitions.reference.license-url`](#definitionsreferencelicense-url)
- [`definitions.reference.loc-end`](#definitionsreferenceloc-end)
- [`definitions.reference.loc-start`](#definitionsreferenceloc-start)
- [`definitions.reference.location`](#definitionsreferencelocation)
- [`definitions.reference.medium`](#definitionsreferencemedium)
- [`definitions.reference.month`](#definitionsreferencemonth)
- [`definitions.reference.nihmsid`](#definitionsreferencenihmsid)
- [`definitions.reference.notes`](#definitionsreferencenotes)
- [`definitions.reference.number`](#definitionsreferencenumber)
- [`definitions.reference.number-volumes`](#definitionsreferencenumber-volumes)
- [`definitions.reference.pages`](#definitionsreferencepages)
- [`definitions.reference.patent-states`](#definitionsreferencepatent-states)
- [`definitions.reference.pmcid`](#definitionsreferencepmcid)
- [`definitions.reference.publisher`](#definitionsreferencepublisher)
- [`definitions.reference.recipients`](#definitionsreferencerecipients)
- [`definitions.reference.repository`](#definitionsreferencerepository)
- [`definitions.reference.repository-artifact`](#definitionsreferencerepository-artifact)
- [`definitions.reference.repository-code`](#definitionsreferencerepository-code)
- [`definitions.reference.scope`](#definitionsreferencescope)
- [`definitions.reference.section`](#definitionsreferencesection)
- [`definitions.reference.senders`](#definitionsreferencesenders)
- [`definitions.reference.start`](#definitionsreferencestart)
- [`definitions.reference.status`](#definitionsreferencestatus)
- [`definitions.reference.term`](#definitionsreferenceterm)
- [`definitions.reference.thesis-type`](#definitionsreferencethesis-type)
- [`definitions.reference.title`](#definitionsreferencetitle)
- [`definitions.reference.translators`](#definitionsreferencetranslators)
- [`definitions.reference.type`](#definitionsreferencetype)
- [`definitions.reference.type`](#definitionsreferencetype)
- [`definitions.reference.url`](#definitionsreferenceurl)
- [`definitions.reference.version`](#definitionsreferenceversion)
- [`definitions.reference.volume`](#definitionsreferencevolume)
- [`definitions.reference.volume-title`](#definitionsreferencevolume-title)
- [`definitions.reference.year`](#definitionsreferenceyear)
- [`definitions.reference.year-original`](#definitionsreferenceyear-original)
- [`definitions.region`](#definitionsregion)
- [`definitions.swh-identifier`](#definitionsswh-identifier)
- [`definitions.tel`](#definitionstel)
- [`definitions.url`](#definitionsurl)
- [`definitions.version`](#definitionsversion)
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

- type: string
- description: A description of the software or dataset.

Usage example:

```yaml
abstract: This software implements methods to do things.
```

### `authors`

- type: Array of [#definitions.person](#definitions.person) and/or [#definitions.entity](#definitions.entity) objects.
- description: The authors of a software or dataset.

Usage example:

```yaml
authors:
  - given-names: Stephan
    family-names: Druskat
  - name: "The Research Software project"
```

### `cff-version`

- type: string
- description: The Citation File Format schema version that the `CITATION.cff` file adheres to for providing the citation metadata.

Usage example:

```yaml
cff-version: 1.2.0
```

### `commit`

- type: string
- description: The commit hash or revision number of the software version

Usage example:

```yaml
commit: 1ff847d81f29c45a3a1a5ce73d38e45c2f319bba
```
```yaml
commit: "Revision: 8612"
```

### `contact`

- type: ...
- description: ...

Usage example:

```yaml
```

### `date-released`

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- description: An address.


Usage example:

```yaml
```

### `definitions.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- description: An alias.

Usage example:

```yaml
```

### `definitions.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- description: A city.

Usage example:

```yaml
```

### `definitions.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: Nonempty string.
- description: The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.

Usage example:

```yaml
```

### `definitions.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: enum
- description: The ISO 3166-1 alpha-2 country code for a country.

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
- description: A date.

Usage example:

```yaml
```

### `definitions.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: string
- description: The DOI of the work (i.e., `10.5281/zenodo.1003150`, not the resolver URL `http://doi.org/10.5281/zenodo.1003150`).

Usage example:

```yaml
doi: "10.5281/zenodo.1003150"
```

### `definitions.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: string
- description: An email address

Usage example:

```yaml
```

### `definitions.entity`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.entity.address`

See [`definitions.address`](#definitionsaddress).

### `definitions.entity.alias`

See [`definitions.alias`](#definitionsalias).

### `definitions.entity.city`

See [`definitions.city`](#definitionscity).

### `definitions.entity.country`

See [`definitions.country`](#definitionscountry).

### `definitions.entity.date-end`

See [`definitions.date`](#definitionsdate).

### `definitions.entity.date-start`

See [`definitions.date`](#definitionsdate).

### `definitions.entity.email`

See [`definitions.email`](#definitionsemail).

### `definitions.entity.fax`

See [`definitions.fax`](#definitionsfax).

### `definitions.entity.location`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.entity.name`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.entity.orcid`

See [`definitions.orcid`](#definitionsorcid).

### `definitions.entity.post-code`

See [`definitions.post-code`](#definitionspost-code).

### `definitions.entity.region`

See [`definitions.region`](#definitionsregion).

### `definitions.entity.tel`

See [`definitions.tel`](#definitionstel).

### `definitions.entity.website`

See [`definitions.url`](#definitionsurl).

### `definitions.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.identifier-description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.license-enum`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.orcid.description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.address`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.affiliation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.alias`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.city`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.country`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.email`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.family-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.fax`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.given-names`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.name-particle`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.name-suffix`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.orcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.person.website`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.post-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.abbreviation`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

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

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.collection-doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.collection-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.collection-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.commit`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.conference`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.contact`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.copyright`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.data-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.database-provider`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.database.description`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.date-accessed`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.date-downloaded`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.date-published`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.date-released`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.department`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.doi`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.edition`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.editors`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.editors-series`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.entry`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.filename`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.format`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.identifiers`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.institution`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.isbn`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.issn`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.issue`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.issue-date`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.issue-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.journal`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.keywords`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.languages`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.license`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.license-url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.loc-end`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.loc-start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.location`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.medium`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.month`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.nihmsid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.notes`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.number`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.number-volumes`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.pages`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.patent-states`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.pmcid`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.publisher`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.recipients`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.repository`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.repository-artifact`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.repository-code`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.scope`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.section`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.senders`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.start`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.status`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.term`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.thesis-type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.translators`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.type`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.volume`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.volume-title`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.year`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.reference.year-original`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.region`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.swh-identifier`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.tel`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.url`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: ...
- description: ...

Usage example:

```yaml
```

### `definitions.version`

`definitions` and its subkeys should not be used directly in `CITATION.cff` files.

- type: string or number
- description: ...

Usage example:

```yaml
```

### `doi`

- type: ...
- description: ...

Usage example:

```yaml
```

### `identifiers`

- type: ...
- description: ...

Usage example:

```yaml
```

### `keywords`

- type: ...
- description: ...

Usage example:

```yaml
```

### `license`

- type: ...
- description: ...

Usage example:

```yaml
```

### `license-url`

- type: ...
- description: ...

Usage example:

```yaml
```

### `message`

- type: ...
- description: ...

Usage example:

```yaml
```

### `preferred-citation`

- type: ...
- description: ...

Usage example:

```yaml
```

### `references`

Array of [`#definitions.reference`](#definitions.reference).

### `repository`

- type: ...
- description: ...

Usage example:

```yaml
```

### `repository-artifact`

- type: ...
- description: ...

Usage example:

```yaml
```

### `repository-code`

- type: ...
- description: ...

Usage example:

```yaml
```

### `title`

- type: ...
- description: ...

Usage example:

```yaml
```

### `type`

- type: ...
- description: ...

Usage example:

```yaml
```

### `url`

- type: ...
- description: ...

Usage example:

```yaml
```

### `version`

- type: ...
- description: ...

Usage example:

```yaml
```
