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
