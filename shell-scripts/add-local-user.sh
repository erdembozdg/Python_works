#!/bin/bash

if [[ "${UID}" -ne 0 ]]
then
    echo 'Please run with sudo or as root'
    exit 1
fi

if [[ ${#} -lt 1 ]]
then
    echo "You need to set at least one parameter"
    exit 1
fi

for USER_NAME in "${@}"
do
    PASSWORD=$(date +%s%N | sha256sum | head -c48)
    echo "${USER_NAME} ${PASSWORD}"
done

if [[ "${?}" -ne 0 ]]
then
    echo 'Something went wrong...'
fi

while [[ "${#}" -gt 0 ]]
do
    echo "Number of parameters: ${#}"
    echo "Parameter 1: ${1}"
    echo "Parameter 1: ${2}"
    echo
    shift
done

passwd -e ${USER_NAME}