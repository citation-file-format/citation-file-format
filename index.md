---
---

{% include toc %}

# Citation File Format (CFF)

Citation File Format is a human- and machine-readable file format in [YAML 1.2](http://www.yaml.org/spec/1.2/spec.html) which provides
citation metadata for software. It is maintained openly on GitHub:
<https://github.com/citation-file-format>.

The current version is [{{ site.current }}](/{{ site.current }}/), for which there is a [detailed format specification](/{{ site.current }}/).

## Example

If you want to make your software easily citable, you can put a file called
`CITATION.cff` in the root of your repository. This file should provide at least the
minimally necessary metadata to cite your software. For example:

{% highlight yaml %}
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
{% endhighlight %}

A CFF file can also be used to record much more information about your software. For
an overview of what software metadata can be supplied with the
Citation File Format, please see [the current version of the format specifications](/{{ site.current }}/).

## Tools

There are a number of tools that can help you work with the Citation File Format to perform useful tasks: generate a `CITATION.cff` file from a [DOI](http://www.doi.org/), convert CFF files to formats required by reference management software', or validate `CITATION.cff` files. For further information, please see [the CFF GitHub repository](https://github.com/citation-file-format/citation-file-format#tools).

## Status

The spectrum of available concepts for software citation metadata files reaches
from non-standardized `CITATION` files as suggested by Robin
Wilson {% cite citation-files %}[^no-file-no-use] to full transitive credit encoded in JSON-LD
{% cite transitive-credit-json-ld %}.

Along this spectrum, Citation File Format is located somewhere between these two extremes as it adds
machine-readability and thus a greater re-use potential to `CITATION` files,
but does not offer transitive credit capabilities (yet), or support for all
citation use cases as outlined by {% cite principles --style ./_bibliography/apa-text.csl %}.

Citation File Format aims at providing a practical solution, and human-friendly properties such
as readability and writability, for the most common software citation use
cases, i.e., *1. Use software for a paper*, *2. Use software in/with new software*,
and *15. Store software entry* (cf. Table 2, {% cite principles --style ./_bibliography/apa-text.csl -l 6 %}).

The basic structure of Citation File Format (i.e., having a *message* and one or more
*references*) explicitly reflects the structure of plain-text `CITATION` files
and manifests its status as a compromise between what is currently *useful* and
*usable*, and what is *desired* (fully transitive credit and attribution). As such, it has value both as a discrete format with everyday application and as a input format populating other citation formats.

## Context

Software citations enhance the dissemination of code, improve software sustainability and ensure authors receive credit for development work. The Citation File Format is an indirect outcome of the discussion group "DS3. Development and
implementation of a standard format for CITATION files." at the [Workshop on
Sustainable Software for Science: Practice and Experiences
(WSSSPE5.1)](http://wssspe.researchcomputing.org.uk/wssspe5-1/) (6 September
2017, Manchester, UK). The group discussed the potential and outlined
requirements for a format for machine-readable CITATION files,
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

One requirement for the [blog post](http://software.ac.uk/blog/) was to be able to make a concrete suggestion
for a format for these machine-readable CITATION files, which triggered the
development of Citation File Format.

[^no-file-no-use]: Not providing a file with software citation metadata is not considered a valid option here.

## Contributing

Contributions to CFF are welcome! Please have a look at the 
[guidelines for contributing](https://github.com/citation-file-format/citation-file-format/blob/master/CONTRIBUTING.md).

# References

{% bibliography --cited %}
