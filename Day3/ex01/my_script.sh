#!/bin/bash

echo "Using pip version:"
pip3 --version

INSTALL_DIR="./local_lib"
LOG_FILE="install.log"
REPO_URL="git+https://github.com/jaraco/path.py.git"

echo "Installing path.py from GitHub into $INSTALL_DIR..."
pip3 install --upgrade --force-reinstall --target="$INSTALL_DIR" "$REPO_URL" > "$LOG_FILE" 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Installation successful. Running Python program..."
    PYTHONPATH=./local_lib python3 my_program.py
else
    echo "Installation failed. Check $LOG_FILE for details."
fi
