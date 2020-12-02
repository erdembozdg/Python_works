#!/bin/bash

awk '{avg=($2+$3+$4)/3; print $0, ":", (avg<50)?"FAIL":(avg<80)?"B":"A"}'
awk '{if ($4 !~ /[0-9]/) print "Not all scores are available for", $1}' 
awk '{print $1, ":", ($2<50||$3<50||$4<50) ? "Fail" : "Pass"}'
awk 'ORS=NR%2?";":"\n"'