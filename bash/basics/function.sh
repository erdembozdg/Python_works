#!/bin/bash

create_files() {
    echo "Creating $1"
    touch $1
    chmod 400 $1

    echo "Creating $2"
    touch $2
    chmod 600 $2
}
create_files a.txt b.txt

function lines_in_file() {
    grep -c "$1" "$2"
}

n=$(lines_in_file "erdem" "/etc/passwd")
echo $n
