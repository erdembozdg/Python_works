#!/bin/bash
if [[ $# -eq 1 ]]; then 
if [ -f "$1" ]; then
    echo "The argument is a file, displaying its content"
    sleep 1
    cat $1
elif [ -d "$1" ]; then 
    echo "The argument is a directory, running ls -l ..."
    sleep 1
    ls -l $1
else
    echo "The argument ($1) is neither a file nor a directory"
fi
fi

read -p "Enter your age " age 

if [[ $age -lt 18 ]] && [[ $age -gt 0 ]]; then
    echo "You are minor"
elif [[ $age -eq 18 ]]; then
    echo "Congratulations, you have just become major"
else
    echo "You are major"
fi

output=$(ping -c 3 $1)

if [[ $output == *"100% packet loss"* ]]
then
    echo "The network connection to $1 is not working."
else
    echo "The network connection to $1 is working."
fi
