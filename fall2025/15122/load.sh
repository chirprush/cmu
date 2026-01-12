#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "Please specify an AndrewID"
else
    sshfs "$1@linux.andrew.cmu.edu:/afs/andrew.cmu.edu/usr19/$1/" remote
fi
