#!/bin/bash 

echo "I am in $0 ${BASH_SOURCE[0]}"



if [[ ! -e venv ]]; then
    echo "Virtualenv does not exist. Creating it."
    
    if hash virtualenv 2>/dev/null; then
        echo "Virtualenv found."
        virtualenv venv
    else
        echo "virtualenv could not be found. You need to install virtualenv and have it in your path."
        exit 1
    fi

fi
