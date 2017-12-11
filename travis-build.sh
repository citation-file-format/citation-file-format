#!/bin/bash

# enable error reporting to the console
set -e

# Build Jekyll site
echo "Build Jekyll site"
gem install bundler
bundle install
bundle exec jekyll build

## push
echo "Push _site"
cd _site
git config user.email "travis-ci@sdruskat.net"
git config user.name "Travis CI"
git add --all
git commit -a -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --force origin master
