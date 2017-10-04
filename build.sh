#!/bin/bash
## Create local copy of index.md
cp index.md pandoc-index.md

## Replace Liquid-style citations with Pandoc-style citations, keeping page numbers
VERSION=$(grep -m 1 "version: " index.md | sed 's/version: //g')
echo $VERSION
ssed -R -i -e 's/ %}/\]/g' pandoc-index.md
ssed -R -i -e 's/ -l(?= \d)/, p\./g' pandoc-index.md
ssed -R -i -e 's/{% cite /\[@/g' pandoc-index.md
## Replace liquid version with real version string
ssed -R -i -e 's,{{ page\.version }},'"$VERSION"',g' pandoc-index.md

## Build PDF from tmp file
pandoc \
	--latex-engine=xelatex \
	--toc \
	--toc-depth=4 \
	--filter pandoc-citeproc \
	--bibliography=./_bibliography/references.bib \
	--csl=./_bibliography/ieee-with-url.csl \
	--metadata date="`date '+%d %B %Y'`" \
	--template=./template/default.latex \
	-o cff-specifications.pdf \
	pandoc-index.md

## Move PDF to final destination
mv ./cff-specifications.pdf ./assets/pdf/cff-specifications.pdf

## Remove tmp file
rm pandoc-index.md
exit 0
