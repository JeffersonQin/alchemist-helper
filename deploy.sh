#!/bin/bash
# clone repo to current folder
git clone $1 .
# obtain shell script path
SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)
# convert python 3.9 typing to 3.7 version
python $SCRIPT_DIR/typing37.py .
