#!/bin/bash
clear
echo "======================================================="
echo "             LUNAR TOOL KIT SETUP (LINUX/TERMUX)       "
echo "======================================================="
echo ""

if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found. Installing Python and pip..."
    if command -v apt &> /dev/null
    then
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif command -v pkg &> /dev/null
    then
        pkg update
        pkg install -y python
    fi
fi

echo "Installing Python dependencies..."
pip3 install -r requirements.txt
echo ""
echo "======================================================="
echo "Setup Complete! You can now run ./start.sh"
echo "======================================================="
