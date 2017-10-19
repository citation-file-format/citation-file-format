#!/bin/bash

# enable error reporting to the console
set -e

# Clone repo
git clone https://${GITHUB_TOKEN}@github.com/citation-file-format/citation-file-format.github.io.git --branch master _site


# Set up and build custom pandoc (for fix of https://github.com/jgm/pandoc/issues/3529)
# git clone https://github.com/jgm/pandoc.git
# cd pandoc
# git checkout 181d737
# stack setup
# stack install --flag pandoc:embed_data_files
# cd ..

# Run the Python script that converts all specifications.md files to PDF
# pip3 install pypandoc
# pip3 install frontmatter
# python3 --version
echo "Build PDFs"
python build-pdfs.py

# Build Jekyll
echo "Build Jekyll site"
bundle install
bundle exec jekyll build
# bundle exec jekyll build

## push
echo "Push PDFs"
cd _site
git config user.email "travis-ci@sdruskat.net"
git config user.name "Travis CI"
git add --all
git commit -a -m "Travis #$TRAVIS_BUILD_NUMBER"
ls -la ./assets/pdf
git push --force origin master
