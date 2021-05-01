#!/bin/bash 

i=0
while [[ $i -lt 10 ]]
do
    echo "i: $i"
    ((i++))
done

while
do
    if $(pgrep -l $1); then
        echo "The process \"$1\" is running"
    else
        echo "The process \"$1\" is not running"
    fi
done