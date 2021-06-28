<!--
SPDX-FileCopyrightText: © 2017ff. Stephan Druskat, Jurriaan H. Spaaks, and the Citation File Format contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Citation File Format (CFF) - Schema Guide

The **Citation File Format (CFF)** is a file format to provide
**citation metadata for software** and datasets.

This is the *Citation File Format Schema Guide*.
It fully specifies the Citation File Format (*CFF*) - Version 1.2.0.

New and changed features in comparison with the previous version are marked with 🆕.

# §1 Format

1. CFF files are named `CITATION.cff`.
2. CFF files are implemented in [YAML 1.2](http://yaml.org/spec/1.2/spec.html).  
You can check if your file is valid YAML on https://www.yamllint.com/.

# §2 Schema

1. The CFF schema is formally defined in a [JSON Schema](https://json-schema.org/) file: [`schema.json`](schema.json) (*the schema*). 🆕  
The schema contains examples and descriptions for all fields in a CFF file.

# §3 Structure

1. CFF files have three main sections:
   1. **Citation metadata** for the software or dataset they describe
   2. A list of **references** for the software or dataset they describe (*optional*)
   3. A **preferred citation** (*optional*) 🆕

# §4 Fields

1. CFF fields are (nested) YAML maps.

> ```yaml
> field: value
> array-field:
>   - value
>   - value
> nested-array-field:
>   - nested-field: value
>     nested-field-2: value
> ```

2. The order of fields in the file is arbitrary, the order suggested for best human-readability is given in the table below.
3. While string values should generally be quoted with double-quotes (`"string value"`), 
it is permissible to *not* quote string values when the value cannot be mistaken for being of another type.
Therefore, all of the following examples are valid string values in CFF.

> ```yaml
> field: "String"
> field: String
> field: "1.2.0" # E.g., a semantic version number
> field: 1.2.0

## §4.1 Required citation metadata fields

### `authors` (*required*)

- **array of [`person`](#person) and/or [`entity`](#entity)**  

> *The authors of a software or dataset.*  
> ```yaml
> authors:
>   - given-names: Stephan
>     family-names: Druskat
>   - name: "The Research Software project"
> ```

### `cff-version` (*required*)

- **string**

> *The version of CFF used for providing the citation metadata.*
> ```yaml
> cff-version: "1.2.0"
> ```

### `message` (*required*)

- **string**

> *A message to the (human) reader of the file to let them know what to do with the citation metadata.*
> ```yaml
> message: "If you use this software, please cite it using the metadata from this file."
> ```

### `title` (*required*)

## §4.2 Optional citation metadata fields

### `abstract`

- **string**  

> *A description of the software or dataset.*  
> `abstract: "Research software to do research with."`

### `commit`

### `contact`

### `date-released`

### `doi`

### `identifiers`

### `keywords`

### `license`

### `license-url`

### `repository`

### `repository-artifact`

### `repository-code`

### `type` 🆕

### `url`

### `version`

## §4.3 Reference fields

### `references`

## §4.4 Preferred citation fields

### `preferred-citation` 🆕

# §5 Definitions

1. Definitions are simple or complex objects that can be used as values for fields.
2. CFF defines the following objects.

### `address`

### `alias`

### `city`

### `commit`

### `country`

### `date`

### `doi`

### `email`

### `entity`

### `fax`

### `identifier`

### `identifier-description` ?

### `license`

### `license-enum` ?

### `orcid`

### `person`

### `post-code`

### `reference` ?

### `region`

### `swh-identifier` ?

### `tel`

### `url`

### `version`



# File structure

`CITATION.cff` files represent YAML 1.2 dictionaries ("maps") with
the keys listed in the table below. Note that the order of the keys is arbitrary,
and that most YAML linters
will re-order the keys alphabetically.

The primary keys are used to specify

- the version of CFF in use (`cff-version`);
- a message which should be conveyed to the user of the software,
along the lines of "If you use this software, please cite it as follows" (`message`);
- the citation metadata for the software version itself, according to [Smith et al., 2016](https://doi.org/10.7717/peerj-cs.86),
i.e., metadata that can be picked up in a CodeMeta JSON file;
- optionally, a list of references which should be cited in different use cases or scopes, e.g., a software paper describing the abstract concepts of the software (`references`).


### `cff-version` (**required**)

`cff-version` must specify the exact version of the
Citation File Format that is used for the file.

```yaml
cff-version: 1.1.0
```

### `message` (**required**)

`message` must specify instructions to users on how
to cite the software the CITATION.cff file is associated
with.

```yaml
message: "Please cite the following works when using this software."
```

### Software citation metadata (**required**)

CFF provides the following keys for software citation metadata.

  | CFF key                 | required | CFF data type                                                                                                                       | Description                                                                                                                                                                     |
  | ----------------------- | :---------:|-------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `abstract`              | |String                                                                                                                              | A description of the software (version)                                                                                                                                         |
  | `authors`               |● |Collection of [entity](#entity-objects) or [person](#person-objects) objects                                                        | The author(s) of the software                                                                                                                                                   |
  | `commit`                | |String                                                                                                                              | The commit hash or revision number of the software version                                                                                                                      |
  | `contact`               | |Collection of [entity](#entity-objects) or [person](#person-objects) objects                                                        | The contact person, group, company, etc. for the software version                                                                                                               |
  | `date-released`         |● |Date                                                                                                                                | The release date of the software version                                                                                                                                        |
  | `doi`                   | |String                                                                                                                              | The DOI of the work (not the resolver URL, i.e., *10.5281/zenodo.1003150*, not *http://doi.org/10.5281/zenodo.1003150*)                                                         |
  | `identifiers`                   | |Collection of [identifier](#identifier-objects) objects                                                                                                                              | The persistent identifiers of the work (for identifiers that are not DOIs)                                                         |
  | `keywords`              | |Collection of strings                                                                                                               | Keywords pertaining to the software version                                                                                                                                     |
  | `license`               | |[SPDX](https://spdx.org/) [License List](https://spdx.org/licenses/) Identifier string                                              | The license the software version is licensed under                                                                                                                              |
  | `license-url`           | |String (URL)                                                                                                                        | The URL of the license text under which the software version is licensed (only for non-standard licenses not included in the [SPDX License List](https://spdx.org/licenses/))   |
  | `repository`            | |String (URL)                                                                                                                        | The URL to the software version in a repository (when the repository is neither a source code repository or a build artifact repository)                                        |
  | `repository-code`       | |String (URL)                                                                                                                        | The URL to the software version in a source code repository                                                                                                                     |
  | `repository-artifact`   | |String (URL)                                                                                                                        | The URL to the software version in a build artifact/binary/release repository                                                                                                   |
  | `title`                 |● |String                                                                                                                              | The name of the software (may include a specific name for the software version)                                                                                                 |
  | `url`                   | |String (URL)                                                                                                                        | The URL to a landing page/website for the software version                                                                                                                      |
  | `version`               |● |String                                                                                                                              | The version of the software                                                                                                                                                       |


### `references` (**optional**)

Provides an optional list of references pertaining to the software version, or the software itself, e.g., a dependency of the software, a software paper describing the abstract concepts of the software, a paper describing an algorithm that has been implemented in the software version, etc.

A reference item, i.e., an item in the list under `references`, must at least
specify values for the following mandatory keys: `type`, `authors`, `title`.

`type` must specify the type of the referenced work. For a list of available
values, cf. [reference types](#reference-types).

`authors` must specify a list of [entity](#entity-objects) or [person objects](#person-objects).

`title` must specify the title of the referenced work.

Example:

```yaml
cff-version: 1.0.3
message: "Please cite the following works when using this software."
...
references:
  - type: book
    authors:
      - ...
    title: The science of citation
  - type: software
    authors:
      - ...
    title: Software Citation Tool
```


Additionally, it can contain any further [reference keys](#reference-keys).

## Reference keys

CFF defines the following reference keys.

  |         CFF Key         |                                  CFF Data Type                                   |                                     Description                                     |
  |-------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
  | `abbreviation`          | String                                                                           | The abbreviation of the work                                                        |
  | `abstract`              | String                                                                           | The abstract of a work                                                              |
  | `authors`               | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The author of a work                                                                |
  | `collection-doi`        | String                                                                           | The DOI of a collection containing the work                                        |
  | `collection-title`      | String                                                                           | The title of a collection or proceedings                                            |
  | `collection-type`       | String                                                                           | The type of a collection                                                            |
  | `commit`                | String                                                                           | The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work       |
  | `conference`            | *[Entity object](#entity-objects)*                                               | The conference where the work was presented                                         |
  | `contact`               | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The contact person, group, company, etc. for a work                                 |
  | `copyright`             | String                                                                           | The copyright information pertaining to the work                                    |
  | `data-type`             | String                                                                           | The data type of a data set                                                         |
  | `database`              | String                                                                           | The name of the database where a work was accessed/is stored                        |
  | `database-provider`     | *[Entity object](#entity-objects)*                                               | The provider of the database where a work was accessed/is stored                    |
  | `date-accessed`         | Date                                                                             | The date the work has been last accessed                                            |
  | `date-downloaded`       | Date                                                                             | The date the work has been downloaded                                               |
  | `date-published`        | Date                                                                             | The date the work has been published                                                |
  | `date-released`         | Date                                                                             | The date the work has been released                                                 |
  | `department`            | String                                                                           | The department where a work has been produced                                       |
  | `doi`                   | String                                                                           | The DOI of the work                                                                 |
  | `edition`               | String                                                                           | The edition of the work                                                             |
  | `editors`               | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The editors of a work                                                               |
  | `editors-series`        | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The editors of a series in which a work has been published                          |
  | `end`                   | Integer                                                                          | The end page of the work                                                            |
  | `entry`                 | String                                                                           | An entry in the collection that constitutes the work                                |
  | `filename`              | String                                                                           | The name of the electronic file containing the work                                 |
  | `format`                | String                                                                           | The format in which a work is represented                                           |
  | `identifiers`                   |Collection of [identifier](#identifier-objects) objects                                                                                                                              | The persistent identifiers of the work (for identifiers that are not DOIs)                                                        |
  | `institution`           | *[Entity object](#entity-objects)*                                               | The institution where a work has been produced or published                         |
  | `isbn`                  | String                                                                           | The ISBN of the work                                                                |
  | `issn`                  | String                                                                           | The ISSN of the work                                                                |
  | `issue`                 | Integer                                                                          | The issue of a periodical in which a work appeared                                  |
  | `issue-date`            | String                                                                           | The publication date of the issue of a periodical in which a work appeared - see note below |
  | `issue-title`           | String                                                                           | The name of the issue of a periodical in which the work appeared                    |
  | `journal`               | String                                                                           | The name of the journal/magazine/newspaper/periodical where the work was published  |
  | `keywords`              | Collection of strings                                                            | Keywords pertaining to the work                                                     |
  | `languages`             | Collection of ISO 639 [*language strings*](#language-strings)                    | The language of the work                                                            |
  | `license`               | *[License string](#license-strings)*                                             | The license under which a work is licensed                                          |
  | `license-url`           | String (*URL*)                                                                   | The URL of the license text under which a work is licensed                          |
  | `location`              | *[Entity object](#entity-objects)*                                               | The location of the work                                                            |
  | `loc-start`             | Integer                                                                          | The line of code in the file where the work starts                                  |
  | `loc-end`               | Integer                                                                          | The line of code in the file where the work ends                                    |
  | `medium`                | String                                                                           | The medium of the work                                                              |
  | `month`                 | Integer                                                                          | The month in which a work has been published                                        |
  | `nihmsid`               | String                                                                           | The NIHMSID of a work                                                               |
  | `notes`                 | String                                                                           | Notes pertaining to the work                                                        |
  | `number`                | String                                                                           | The accession number for a work                                                     |
  | `number-volumes`        | Integer                                                                          | The number of volumes making up the collection in which the work has been published |
  | `pages`                 | Integer                                                                          | The number of pages of the work                                                     |
  | `patent-states`         | Collection of strings                                                            | The states for which a patent is granted                                            |
  | `pmcid`                 | String                                                                           | The PMCID of a work                                                                 |
  | `publisher`             | *[Entity object](#entity-objects)*                                               | The publisher who has published the work                                            |
  | `recipients`            | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The recipient of a personal communication                                           |
  | `repository`            | String (*URL*)                                                                   | The repository where the work is stored                                             |
  | `repository-code`       | String (*URL*)                                                                   | The version control system where the source code of the work is stored              |
  | `repository-artifact`   | String (*URL*)                                                                   | The repository where the (executable/binary) artifact of the work is stored         |
  | `scope`                 | String                                                                           | The scope of the reference, e.g., the section of the work it adheres to             |
  | `section`               | String                                                                           | The section of a work that is referenced                                            |
  | `senders`               | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The sender of a personal communication                                              |
  | `status`                | *[Status string](#status-strings)*                                               | The publication status of the work                                                  |
  | `start`                 | Integer                                                                          | The start page of the work                                                          |
  | `term`                  | String                                                                           | The term being referenced if the work is a dictionary or encyclopedia        |
  | `thesis-type`           | String                                                                           | The type of the thesis that is the work                                             |
  | `title`                 | String                                                                           | The title of the work                                                               |
  | `translators`           | Collection of *[entity](#entity-objects)* or *[person objects](#person-objects)* | The translator of a work                                                            |
  | `type`                  | *[Reference types](#reference-types) string*                                     | The type of the work                                                                |
  | `url`                   | String (*URL*)                                                                   | The URL of the work                                                                 |
  | `version`               | String                                                                           | The version of the work                                                             |
  | `volume`                | Integer                                                                          | The volume of the periodical in which a work appeared                               |
  | `volume-title`          | String                                                                           | The title of the volume in which the work appeared                                  |
  | `year`                  | Integer                                                                          | The year in which a work has been published                                         |
  | `year-original`         | Integer                                                                          | The year of the original publication                                                |

### Notable reference keys

**`conference`**, **`database‑provider`**, **`institution`**, **`publisher`**

These keys take an [entity object](#entity-objects) as value. Entity objects
reference named entities and provide a fixed set of keys, such as `name` and
contact information.

Example:

```yaml
references:
  - type: book
    publisher:
      - name: PeerJ
        city: London
        country: GB
        website: https://peerj.com/
```

**`authors`**, **`contact`**, **`editors`**, **`editors-series`**, **`recipients`**,
**`senders`**, **`translators`**

These keys take a collection of entity objects or
[person objects](#person-objects) as value. Person objects
provide a fixed set of keys to reference individuals, including a detailed
set for specifiying personal names, an affiliation, etc.

Example:

```yaml
references:
  - type: software
    authors:
      - family-names: Druskat
        given-names: Stephan
        orcid: https://orcid.org/0000-0003-4925-7248
        affiliation: "Humboldt-Universität zu Berlin"
        email: "mail@sdruskat.net"
        website: http://sdruskat.net
      - family-names: Beethoven
        name-particle: van
        given-names: Ludwig
      - family-names: Fernández de Córdoba
        given-names: Gonzalo
        name-suffix: Jr.
    ...
```

**`type`**, **`languages`**, **`status`**

These keys only take values from a defined set, cf. the respective sections:

- [Reference types](#reference-types)
- [Language strings](#language-strings)
- [Status strings](#status-strings)

**`license‑url`**, **`repository`**, **`repository-code`**, **`repository-artifact`**,
**`url`**

These keys take URL strings as values. URLs will be validated by a regular
expression, such as the one provided in a [GitHub Gist by Diego Perini](https://gist.github.com/dperini/729294).

**`keywords`**

This key takes a collection of strings.

Example:

```yaml
references:
  - type: software
    keywords:
      - linguistics
      - "multi-layer annotation"
      - web service
    ...
```


**`scope`**

A reference item can specify a more detailed scope for the reference, via the
reference key `scope`. This key can be useful if certain references should only
be cited under specific circumstances, e.g., only when a specific package
of the software is used. In such a case, the package would ideally have its own
CFF file, but if this is not possible for whatever reason, the `scope` key
may come in handy.

For a discussion of this key, cf. [issue citation-file-format/citation-file-format#15](https://github.com/citation-file-format/citation-file-format/issues/15).

Example:

```yaml
references:
  - scope: "Cite this paper when you run software X with flag --xy"
    type: article
    ...
```

**`issue-date`**

Specify the date of release of an issue. This key has been left as a plain
string, rather than a formal date type, to allow for text values such as
"November-December 2018".

For a discussion of this key, cf. [issue citation-file-format/citation-file-format#48](https://github.com/citation-file-format/citation-file-format/issues/48).

### Exemplary uses

This section details exemplary use cases for some of the keys to avoid
ambiguity/misuse.

**`abstract`**

- If the work is a journal paper or other academic work: The abstract of the work.
- If the work is a film, broadcast or similar: The synopsis of the work.

**`department`**

- If the work is a thesis: The academic department where the thesis has been produced.
- If the work is a government document: The governmental department which has issued the document.

**`format`**

- If the work is a music file: The digital format in which a musical piece is saved, e.g., MP3.
- If the work is a data set: The digital format in which the data set is saved.
- If the work is a painting: The format of the painting, e.g., the width and height of the canvas.

**`institution`**

- If the work is a report: The institution where the report has been produced.
- If the work is a case: The court where a case has been held.
- If the work is a blog post: The institution responsible for running the blog.
- If the work is a patent, legal rule or similar: The issuing institution of the patent/rule.
- If the work is a grant: The funding agency sponsoring the grant.
- If the work is a thesis: The university where a thesis has been produced.
- If the work is a statute: The institution or geographical unit which the statute adheres to.
- If the work is a conference: The organisation which held the conference.

**`languages`**

- If the work is a book: The language in which the book is written.

**`location`**

- If the work is an artwork: E.g., the museum holding the work.
- If the work is a historical work, illuminated manuscript or similar: The library or archive where the work is held.

**`medium`**

- If the work is an artwork: The medium of the artwork, e.g., "photograph",
"painting", "oil on canvas", etc.
- If the work is a book or similar: Whether it is a printed book or an ebook.

**`month`**

- If the work is a conference: The month in which the conference has been held.
- If the work is a magazine article: The month in which the magazine issue containing the article has been published.

**`number`**

- If the work is a conference paper: E.g., the submission number of the paper.
- If the work is a grant: The grant number provided by the funding agency.
- If the work is a work of art: E.g., the catalogue number provided by a museum holding the artwork.
- If the work is a report: The report number of a report.
- If the work is a patent: The patent number of the work.
- If the work is a historical work, illuminated manuscript or similar: The codex or folio number of a manuscript, or the library identifier for a manuscript.

**`term`**

- If the work is a dictionary or encyclopedia: The term in the dictionary or encyclopedia that is being referenced.

**`title`**

- If the work is a case: The name of the case (e.g., Name v. Name).

**`version`**

- If the work is a software: The version of the referenced software.


## Reference types

|    Reference type string     |                   Description                   |
|------------------------------|-------------------------------------------------|
| **`art`**                      | A work of art, e.g., a painting                 |
| **`article`**                  |                                                 |
| **`audiovisual`**              |                                                 |
| **`bill`**                     | A legal bill                                    |
| **`blog`**                     | A blog post                                     |
| **`book`**                     | A book or e-book                                |
| **`catalogue`**                |                                                 |
| **`conference`**               |                                                 |
| **`conference-paper`**         |                                                 |
| **`data`**                     | A data set                                      |
| **`database`**                 | An aggregated or online database                |
| **`dictionary`**               |                                                 |
| **`edited-work`**              | An edited work, e.g., a book                    |
| **`encyclopedia`**             |                                                 |
| **`film-broadcast`**           | A film or broadcast                             |
| **`generic`**                  | The fallback type                               |
| **`government-document`**      |                                                 |
| **`grant`**                    | A research or other grant                       |
| **`hearing`**                  |                                                 |
| **`historical-work`**          | A historical work, e.g., a medieval manuscript  |
| **`legal-case`**               |                                                 |
| **`legal-rule`**               |                                                 |
| **`magazine-article`**         |                                                 |
| **`manual`**                   | A manual                                        |
| **`map`**                      | A geographical map                              |
| **`multimedia`**               | A multimedia file                               |
| **`music`**                    | A music file or sheet music                     |
| **`newspaper-article`**        |                                                 |
| **`pamphlet`**                 |                                                 |
| **`patent`**                   |                                                 |
| **`personal-communication`**   |                                                 |
| **`proceedings`**              | Conference proceedings                          |
| **`report`**                   |                                                 |
| **`serial`**                   |                                                 |
| **`slides`**                   | Slides, i.e., a published slide deck            |
| **`software`**                 | Software                                        |
| **`software-code`**            | Software source code                            |
| **`software-container`**       | A software container (e.g., a docker container) |
| **`software-executable`**      | An executable software, i.e., a binary/artifact |
| **`software-virtual-machine`** | A virtual machine/vm image                      |
| **`sound-recording`**          |                                                 |
| **`standard`**                 |                                                 |
| **`statute`**                  |                                                 |
| **`thesis`**                   | An academic thesis                              |
| **`unpublished`**              |                                                 |
| **`video`**                    | A video recording                               |
| **`website`**                  |                                                 |


# Objects

## Entity objects

Entity objects can represent different types of entities, e.g.,
a publishing company, or conference. In CFF, they are realized as collections with
a defined set of keys. Only the key `name` is mandatory.

| Entity key   | Entity data type     | optional |
| -            | -                    | :-:      |
| `name`       | String               |          |
| `address`    | String               | ●        |
| `city`       | String               | ●        |
| `region`     | String               | ●        |
| `post-code`  | String               | ●        |
| `country`    | String               | ●        |
| `orcid`      | String (*ORCID URL*) | ●        |
| `email`      | String               | ●        |
| `tel`        | String               | ●        |
| `fax`        | String               | ●        |
| `website`    | String (*URL*)       | ●        |
| `date-start` | Date                 | ●        |
| `date-end`   | Date                 | ●        |
| `location`   | String               | ●        |


### Exemplary uses

**`address`**

- To be used for street names and house numbers, etc.

**`region`**

- To be used for, e.g., states (as in US states or German federal states).

**`post-code`**

- The post code or zip code of an address.

**`country`**

- The ISO 3166-1 alpha-2 country code for a country. A list of ISO 3166-1
alpha-2 codes can be found at
[Wikipedia:ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

Example:

```yaml
references:
  - type: book
    publisher:
      - name: PeerJ
        city: London
        country: GB
```

**`date-start`** and **`date-end`**

- The start and end date of, e.g., a conference. This must be formatted
according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), e.g.,
`YYYY-MM-DD`, or `2017-10-04T16:20:57+00:00`.

**`orcid`**

The ORCID iD is expressed as an https URI, i.e. the 16-digit identifier is
preceded by ``https://orcid.org/``. A hyphen is inserted every 4 digits of the
identifier to aid readability (See https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier,
section "Expressing the ORCID iD").

Example:

```yaml
orcid: https://orcid.org/0000-0001-2345-6789
```

## Person objects

A person object represents a person. In CFF, person objects are realized as
collections with a defined set of keys.

| Person key      | Person data type     |
| -               | -                    |
| `family-names`  | String               |
| `given-names`   | String               |
| `alias`         | String               |
| `name-particle` | String               |
| `name-suffix`   | String               |
| `affiliation`   | String               |
| `address`       | String               |
| `city`          | String               |
| `region`        | String               |
| `post-code`     | String               |
| `country`       | String               |
| `orcid`         | String (*ORCID URL*) |
| `email`         | String               |
| `tel`           | String               |
| `fax`           | String               |
| `website`       | String (*URL*)       |


### Exemplary uses

**Name keys**

CFF aims to implement a culturally neutral model for personal names,
according to the
[suggestions on splitting personal names by the W3C](https://www.w3.org/International/questions/qa-personal-names)
and the implementation of personal name splitting in
BibTeX ([Hufflen, 2006](https://www.tug.org/TUGboat/tb27-2/tb87hufflen.pdf)).

To this end, CFF provides four generic keys to specify personal names:


1. Values for `family-names` specify family names, including combinations of given and
patronymic forms, such as *Guðmundsdóttir* or *bin Osman*; double names with or
without hyphen, such as *Leutheusser-Schnarrenberger* or *Sánchez Vicario*. It
can potentially also specify names that include prepositions or (nobiliary)
particles, especially if they occur in between family names such as in Spanish-
or Portuguese-origin names, such as *Fernández de Córdoba*.
2. Values for `given-names` specify given and any other names.
3. Values for `name-particle` specify nobiliary particles and prepositions, such as in
Ludwig *van* Beethoven or Rafael *van der* Vaart.
4. Values for `name-suffix` specify suffixes such as *Jr.* or *III* (as in
[Frank Edwin Wright *III*](https://en.wikipedia.org/wiki/Tr%C3%A9_Cool)).

Note that these keys may still not be optimal for, e.g., Icelandic names which
do not have the concept of family names, or Chinese generation names, but the
alternative is highly localized customization, which would be counterintuitive
as to CFF's goal to be easily accessible. Thus, it is ultimately the task of CFF
file authors to find the optimal name split in any given case.

**`alias`**

- To specify a person who is only known by an alias such as a username.

**`affiliation`**

- To specify the affiliation of a person, e.g., a university, research centre, etc.

**Address keys**

- Cf. [Entity objects](#entity-objects) for details.

**`orcid`**

- Cf. [Entity objects](#entity-objects) for details.

## Identifier objects

An identifier object represents a persistent identifier. In CFF, identifier objects are realized as
collections with two defined keys, both mandatory.

| Identifier key      | Identifier data type     | optional       |
| -               | -                    | :------------: |
| `type`  | String ([*Identifier type string*](#identifier-type-strings))              |                |
| `value`   | String               |                |


### Exemplary uses

**A Software Heritage identifier**

```yaml
identifiers:
  - type: "swh"
    value: "swh:1:rel:99f6850374dc6597af01bd0ee1d3fc0699301b9f"
```

**An identifier unknown to CFF**

```yaml
identifiers:
  - type: "other"
    value: "my-custom-identifier-1234"
```

# Specified value strings

The keys `status`, `license`, `languages`, and `identifier:type` can only take values
from a fixed set of strings. These are specified below.

## Status strings

Works can have a different status of publication, e.g., journal papers. CFF
specifies the following value strings for the key `status`.

  | Status (String)  |                                     Description                                      |
  |------------------|--------------------------------------------------------------------------------------|
  | `in-preparation` | A work in preparation, e.g., a manuscript (covers drafts)                            |
  | `abstract`       | The abstract of a work                                                               |
  | `submitted`      | A work that has been submitted for publication                                       |
  | `in-press`       | A work that has been accepted for publication but has not yet been published         |
  | `advance-online` | A work that has been published online in advance of publication in the target medium |
  | `preprint`       | A work that has been published as a preprint before peer review                      |

For a work that is complete and has been published, leave `status` unset.

## License strings

License strings must conform with the [SPDX Licenses
list](https://spdx.org/licenses/), i.e., a license must be specified via the
short identifier from the list. If a license is not included in the SPDX
Licenses list, the `license-url` should be provided as a fallback.

Example:

```yaml
references:
  - type: software
    authors:
      - ...
    title: My Research Tool
    license: Apache-2.0
  - type: software
    authors:
      - ...
    title: Obscure Research Tool
    license-url: http://r3s34archs0ft.com/eula
```

## Language strings

Natural languages as a value for the key `languages` are specified via their
respective 3-character [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) code. A list
of ISO 639-3 codes in maintained at
[Wikipedia:List of ISO 639-3 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes).
Alternatively, a language's 2-character
[ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code may be used. A list
of ISO 639-1 codes is maintained at
[Wikipedia:List of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

Example for a work in both English and Daakaka:

```yaml
references:
  - type: book
    ...
    languages:
      - en
      - bpa
```

## Identifier type strings

The key

```yaml
identifiers:
  - type
```

can only take the following values:

- `doi`: Signifies that the `value` string of the identifier typed thus is a valid DOI.
- `url`: Signifies that the `value` string of the identifier typed thus is a valid URL.
- `swh`: Signifies that the `value` string of the identifier typed thus is a valid [Software Heritage identifier](https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html).
- `other`: Signifies that the `value` string of the identifier typed thus is a valid identifier not currently known to CFF.  
If you want to add an identifier type to CFF, please [create a new issue on the CFF GitHub repository](https://github.com/citation-file-format/citation-file-format/issues/new), and suggest a name for the identifier, and ideally also describe its format as a valid regex.

Examples for valid identifiers:

```yaml
identifiers:
  - type: "other"
    value: "other-schema://abcd.1234.efgh.5678"
  - type: "swh"
    value: "swh:1:rel:99f6850374dc6597af01bd0ee1d3fc0699301b9f"
```

