#!/bin/env bash

set -e

FILES=$(find . | grep "CITATION\.cff$")

for FILE in $FILES
do
    echo $FILE && cffconvert --infile $FILE --validate
done