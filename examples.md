### Source code without a DOI

We recognize that there are certain situations where it may not be possible to
follow the recommended best-practice. For example, if (1) the software authors
did not register a DOI and/or release a specific version, or (2) the version of
the software used does not match what is available to cite. In those cases,
falling back on a combination of the repository URL and version number/commit
hash would be an appropriate way to cite the software used ([Smith et al., 2016](https://doi.org/10.7717/peerj-cs.86), p. 12).

```yaml
cff-version: 1.0.3
message: "If you use this MRT alpha snapshot version, please cite."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool Prototype
version: 0.0.1-alpha1-build1507284872
date-released: 2017-12-18
repository-code: https://github.com/doe/mrt
commit: 160d54f9e935c914df38c1ffda752112b5c979a8
```

### Closed-source software without a DOI

For software without a DOI, it is recommended that "the metadata should still
provide information on how to access the specific software, but this may be a
company’s product number or a link to a website that allows the software be
purchased." [Smith et al., 2016](https://doi.org/10.7717/peerj-cs.86), p. 13. Furthermore, "if the version number and
release date are not available, the download date can be used. Similarly, the
contact name/email is an alternative to the location/repository."
([Smith et al., 2016](https://doi.org/10.7717/peerj-cs.86), p. 7).

Hence, for closed-source software without a DOI for which the version number
and release date cannot be determined, a `CITATION.cff` file could look like
this.

```yaml
cff-version: 1.0.3
message:
  If you dare use this commercial, closed-source, strangely versioned
  software in your research, please at least cite it as below.
authors:
  - family-names: Vader
    name-suffix: né Skywalker
    given-names: 'Anakin "Darth"'
title: Opaquity
version: opq-1234-XZVF-ACME-RLY
date-released: 2017-02-28
url: http://www.opaquity.com
contact:
  - name: Dark Side Software
    address: DS-1 Orbital Battle Station, near Scarif
    email: father@imperial-empire.com
    tel: +850 (0)123-45-666
```

### An executable

```yaml
cff-version: 1.0.3
message: "If you use MRT, please cite the following."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool Kickstarter
version: 2.0.4
date-released: 2017-12-18
repository-artifact: https://hu.berlin/nexus/mrt-kickstarter/2.0.4/mrt2-kickstarter.exe
```

### A software container

```yaml
cff-version: 1.0.3
message: "If you use the MRT Docker container, please cite the following."
authors:
  - name: "Humboldt-Universität zu Berlin"
    website: https://www.linguistik.hu-berlin.de/
  - family-names: Doe
    given-names: Jane
title: mrt-iain-m-banks
version: 1.0.4 (Iain M. Banks)
url: https://github.com/doe/docker-brew-mrt/blob/160d54f9e935/iain/Dockerfile
repository: https://hub.docker.hu-berlin.de/_/mrt-iain-m-banks/
date-released: 2017-12-18
```

### Software with a further reference

Where authors wish to encourage citation of an outline paper with citation of their software, we recommend the use of [reference keys](#references-optional) to highlight the existence of further references.

```yaml
cff-version: 1.0.3
message: If you use My Research Tool, please cite both the software and the outline paper.
authors:
  - family-names: Doe
    given-names: Jane
  - family-names: Bielefeld
    name-particle: von
    given-names: Arthur
  - family-names: McAuthor
    given-names: Juniper
    name-suffix: Jr.
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: article
    scope: Cite this paper if you want to reference the general concepts of MRT.
    authors:
      - family-names: Doe
        given-names: Jane
      - family-names: Bielefeld
        name-particle: von
        given-names: Arthur
    title: "My Research Tool: A 100% accuracy syntax parser for all languages"
    year: 2099
    journal: Journal of Hard Science Fiction
    volume: 42
    issue: "13"
    doi: 10.9999/hardscifi-lang.42132
```

### Some references examples

#### art

```yaml
cff-version: 1.0.3
message: "If you use this software, please cite the following."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: art
    authors:
      - family-names: Picasso
        given-names: Pablo
    title: Guernica
    year: 1937
    medium: Oil on canvas
    format: 349.3cm x 776.6cm
    location:
      name: Museo Reina Sofia
      city: Madrid
      country: ES
```

#### article

```yaml
cff-version: 1.0.3
message: If you use this software, please cite it as below.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: article
    authors:
      - family-names: Smith
        given-names: Arfon M.
      - family-names: Katz
        given-names: Daniel S.
        affiliation: "National Center for Supercomputing Applications &
        Electrical and Computer Engineering Department & School of Information
        Sciences, University of Illinois at Urbana-Champaign, Urbana, Illinois,
        United States"
        orcid: https://orcid.org/0000-0001-5934-7525
      - family-names: Niemeyer
        given-names: Kyle E.
      - name: "FORCE11 Software Citation Working Group"
        website: https://www.force11.org/group/software-citation-working-group
    title: "Software citation principles"
    year: 2016
    journal: PeerJ Computer Science
    volume: 2
    issue: e86
    doi: 10.7717/peerj-cs.86
    url: https://doi.org/10.7717/peerj-cs.86
```

#### blog

```yaml
cff-version: 1.0.3
message: If you use this software, please cite the software itself and the blog post.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: blog
    authors:
      - family-names: Doe
        given-names: Jane
    title: "Implement a 100% accuracy syntax parser for all languages? No probs!"
    date-published: 2017-09-23
    url: https://hu-berlin.de/blogs/jdoe/2017/09/23/if-only
    institution:
      name: "Humboldt-Universität zu Berlin"
      city: Berlin
      country: DE
```

#### book

```yaml
cff-version: 1.0.3
message: "If you use MRT for your research, please cite the following book."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: book
    authors:
      - family-names: Doe
        given-names: Jane
    title: "The future of syntax parsing"
    year: 2017
    publisher:
      name: Far Out Publications
      city: Bielefeld
    medium: print
```

#### conference-paper

```yaml
cff-version: 1.0.3
message: If you use this software, please cite the software and the paper.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: conference-paper
    authors:
      - family-names: Doe
        given-names: Jane
    title: "Ultimate-accuracy syntax parsing with My Research Tool"
    year: 2017
    collection-title: "Proceedings of the 1st Conference on Wishful Thinking"
    collection-doi: 10.5281/zenodo.123456
    editors:
      - family-names: Kirk
        given-names: James T.
    conference:
      name: 1st Conference on Wishful Thinking
      location: Spock's Inn Hotel and Bar
      address: 123 Main St
      city: Bielefeld
      region: Jarvis Island
      post-code: "12345"
      country: UM
      date-start: 2017-04-01
      date-end: 2017-04-01
    start: 42
    end: 45
    doi: 10.5281/zenodo.1234
```

#### edited-work

Note that the editors of the edited work must be specified under the `authors`
key. Specific citation styles may or may not attach a suffix to the authors,
such as ", eds." or similar.

```yaml
cff-version: 1.0.3
message: If you use this software, please cite it as below.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: edited-work
    authors:
      - family-names: Doe
        given-names: Jane
    title: "Ultimate-accuracy parsing in practice"
    year: 2017
    publisher:
      name: Far Out Publications
      city: Bielefeld
      country: DE
```

#### report

```yaml
cff-version: 1.0.3
message: If you use this software, please cite it as below.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: report
    authors:
      - name: Fictional Parsing Interest Group, ACME Inc.
    title: "100% accuracy syntax parsing at ACME"
    url: http://www.acme.com/sigs/fp/reports/hpsp.pdf
    year: 2017
    date-accessed: 2017-09-23
```

#### thesis

```yaml
cff-version: 1.0.3
message: If you use this software, please cite it as below.
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: My Research Tool
version: 1.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
references:
  - type: thesis
    authors:
      - family-names: Doe
        given-names: Jane
    title: "A high accuracy syntax parser in Visual Basic"
    thesis-type: PhD
    year: 2017
    department: Dept. of Universal Language Philosophy
    institution:
      name: "Humboldt-Universität zu Berlin"
      city: Berlin
      country: DE
    database: Thesiserver
    date-accessed: 2017-09-23
    date-published: 2017-03-21
    url: http://thesiserver.hu-berlin.de/2017/march/phd/doe-12345
```
