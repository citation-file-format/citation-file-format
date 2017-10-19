---
---

{% include toc %}

# Citation File Format (CFF)

CFF is a human- and machine-readable file format in YAML 1.2 which provides
citation metadata for software. It is maintained openly on GitHub:
<https://github.com/citation-file-format>.

The current version is [{{ site.current }}](/{{ site.current }}/).

## Status

The spectrum of available concepts for software citation metadata files reaches
from non-standardized `CITATION` files as suggested by Robin
Wilson {% cite citation-files %}[^no-file-no-use] to full transitive credit encoded in JSON-LD
{% cite transitive-credit-json-ld %}.

Along this spectrum, CFF is located somewhere between these two extremes as it adds
machine-readability and thus a greater re-use potential to `CITATION` files,
but does not offer transitive credit capabilities (yet), or support for all
citation use cases as outlined by {% cite principles --style ./_bibliography/apa-text.csl %}.

CFF aims at providing a practical solution, and human-friendly properties such
as readability and writability, for the most common software citation use
cases, i.e., *1. Use software for a paper*, *2. Use software in/with new software*,
and *15. Store software entry* (cf. Table 2, {% cite principles --style ./_bibliography/apa-text.csl -l 6 %}).

## Context

CFF is an indirect outcome of the discussion group "DS3. Development and
implementation of a standard format for CITATION files." at the [Workshop on
Sustainable Software for Science: Practice and Experiences
(WSSSPE5.1)](http://wssspe.researchcomputing.org.uk/wssspe5-1/) (6 September
2017, Manchester, UK). The group discussed the potential and outlined
requirements for a format for machine-readable CITATION files[^citation-files],
and has authored a blog post on the subject, which will be published on the
[blog](http://software.ac.uk/blog/) of the [Software Sustainability
Institute](http://software.ac.uk/).

Members of the group were:

- Stephan Druskat (Humboldt-Universität zu Berlin, Germany), *Lead*
- Neil Chue Hong (Software Sustainability Institute, University of Edinburgh, UK)
- Raniere Silva (Software Sustainability Institute, University of Manchester, UK)
- Radovan Bast (University of Tromsø, Norway)
- Andrew Rowley (University of Manchester, UK)
- Alexander Konovalov (University of St. Andrews, UK)

One requirement for the blog post was to be able to make a concrete suggestion
for a format for these machine-readable CITATION files, which triggered the
development of CFF.

[^no-file-no-use]: Not providing a file with software citation metadata is not considered a valid option here.

# References

{% bibliography --cited %}