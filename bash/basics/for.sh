#!/bin/bash

for os in Ubuntu Centos "Kali Linux"
do 
    echo "os is $os"
done

for i in {3..7..1}
do
    echo "num is $i"
done

for item in ./*
do 
    if [[ -f $item ]]; then
        echo "Displaying the contents of the $item"
        sleep 1
        cat $item
        echo "#######################"
    fi
done

for ((i=0;i<10;i++))
do
    echo "i is $i"
done