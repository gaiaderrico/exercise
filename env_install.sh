#!/bin/bash

pretty_print() {
printf "\n%s\n\n" "$1"
}
pretty_print "Starting configuration"
if [[ "$OSTYPE" == darwin* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == linux* ]]; then
    OS="linux"
fi

pretty_print "System: $OS"
if ! command -v python3 > /dev/null; then
    pretty_print "Python not found, installing..."
    if [[ "$OS" == "macos" ]]; then
        brew install python
    else
        sudo apt-get install -y python3
    fi
else
    pretty_print "Python found:"
    python3 --version
fi
if ! command -v pip3 > /dev/null; then
pretty_print "pip3 not found, installing..."
python3 -m ensurepip --upgrade
else 
pretty_print "pip3 found:"
pip3 --version
fi
if ! command -v jupyter > /dev/null; then
    pretty_print "Jupyter not found, installing..."
    if [[ "$OS" == "macos" ]]; then
        brew install jupyterlab
    else
        pip3 install --user notebook
    fi
else
    pretty_print "Jupyter found:"
    jupyter --version
fi

if [[ "$OS" == "macos" ]]; then
    pretty_print "Running brew doctor..."
    brew doctor
fi

pretty_print "Configuration complete!"
