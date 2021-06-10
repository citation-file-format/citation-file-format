
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
