#!/usr/bin/env bash

sum=0
read n

while read line || [[ -n $line ]]; do
    sum=$(( $sum + $line ))
done

printf '%.3f' $(echo "$sum/$n" | bc -l)


