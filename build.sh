#!/bin/bash
pandoc \
	--toc \
	--toc-depth=4 \
	--filter pandoc-citeproc \
	--bibliography=references.bib \
	--template=./template/default.latex \
	-o cff-specifications.pdf \
	index.md

cp ./cff-specifications.pdf ./assets/pdf/
exit 0
