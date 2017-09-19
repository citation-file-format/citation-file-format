#!/bin/bash
pandoc \
	--filter pandoc-citeproc \
	--bibliography=references.bib \
	--template=./template/default.latex \
	-o cff-specifications.pdf \
	index.md

cp ./cff-specifications.pdf ./assets/pdf/
exit 0
