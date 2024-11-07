#!/bin/bash

directory=$1

##ls "$1" | sort -n -t * -k 2

sudo openssl md5 "$1"/* > md5hashlist.txt

cat md5hashlist.txt
