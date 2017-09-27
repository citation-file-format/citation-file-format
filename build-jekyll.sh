#!/bin/bash

# skip if build is triggered by pull request
if [ $TRAVIS_PULL_REQUEST == "true" ]; then
  echo "This is PULL REQUEST, exiting."
  exit 0
fi

# enable error reporting to the console
set -e

# Build PDF
## Create local copy of index.md
cp index.md pandoc-index.md

## Replace Liquid-style citations with Pandoc-style citations, keeping page numbers
ssed -R -i -e 's/ %}/\]/g' pandoc-index.md
ssed -R -i -e 's/ -l(?= \d)/, p\./g' pandoc-index.md
ssed -R -i -e 's/{% cite /\[@/g' pandoc-index.md

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

# cleanup "_site"
rm -rf _site
mkdir _site

# clone remote repo to "_site"
git clone https://${GITHUB_TOKEN}@github.com/sdruskat/citation-file-format.git --branch gh-pages _site

# build with Jekyll into "_site"
gem install jekyll-pandoc
gem install jekyll-scholar
bundle exec jekyll build

# push
cd _site
git config user.email "travis-ci@sdruskat.net"
git config user.name "Travis CI"
git add --all
git commit -a -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --force origin gh-pages
