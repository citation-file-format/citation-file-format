# Citation File Format (CFF)

Format specification for `CITATION` files. `CITATION` files provide reference and citation information for (research/scientific) software.

[Read the specifications](cff-specifications-1.0.pdf).

Build the specifications PDF with [pandoc](https://pandoc.org/):

````
pandoc --filter pandoc-citeproc --bibliography=references.bib -o cff-specifications-1.0.pdf cff-specifications-1.0.md
````
