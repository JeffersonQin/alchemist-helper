#!/bin/bash
# clone repo to tmp folder
mkdir tmp
git clone $1 tmp
# move to current folder
(shopt -s dotglob; mv tmp/* .)
rm -rf tmp
rm -rf .git
# obtain shell script path
SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)
# convert python 3.9 typing to 3.7 version
python $SCRIPT_DIR/typing37.py .
