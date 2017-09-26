#!/bin/bash
pandoc \
	--toc \
	--toc-depth=4 \
	--filter pandoc-citeproc \
	--bibliography=references.bib \
	--metadata date="`date '+%d %B %Y'`" \
	--template=./template/default.latex \
	-o cff-specifications.pdf \
	index.md

mv ./cff-specifications.pdf ./assets/pdf/cff-specifications.pdf
exit 0
