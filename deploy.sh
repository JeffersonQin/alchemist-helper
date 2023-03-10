#!/bin/bash
# clone repo to tmp folder
mkdir tmp
git clone $1 tmp
# checkout to the destination branch if specified
if [ -n "$2" ] ;then
  git -C tmp checkout $2
fi
# move to current folder
(shopt -s dotglob; mv tmp/* .)
rm -rf tmp
rm -rf .git
# obtain shell script path
SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)
# convert python 3.9 typing to 3.7 version
python $SCRIPT_DIR/typing37.py .
