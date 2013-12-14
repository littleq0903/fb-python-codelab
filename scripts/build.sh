#!/bin/bash
# Script to generate package to download
# Author: LittleQ <littleq0903@gmail.com>

TARGET=build
BRANCHES="cp0 cp1 cp2 cp3 cp4"

mkdir -p ${TARGET}

for branch in ${BRANCHES}
do
    mkdir -p ${TARGET}/${branch}
    git archive ${branch} | tar -x -C ${TARGET}/${branch}
done

