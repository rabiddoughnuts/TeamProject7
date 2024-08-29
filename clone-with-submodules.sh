#!/bin/bash

REPO="https://github.com/rabiddoughnuts/TeamProject7.git"

git clone --recurse-submodules "$REPO"

cd "$(basename "$REPO" .git)"

git submodule update --init --recursive
