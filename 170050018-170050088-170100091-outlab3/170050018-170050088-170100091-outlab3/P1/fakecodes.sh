#!/bin/bash


while read line
do
    a="$(head /dev/urandom | tr -dc A-Z | head -c 1)"
    b="$(head /dev/urandom | tr -dc A-Z | head -c 1)"
    c="$(head /dev/urandom | tr -dc 0-9 | head -c 1)"
    echo $line | sed 's/\([[:space:]]\|^\)[A-Z][A-Z][0-9]/\1'$a''$b''$c'/g'
done <"$1"
