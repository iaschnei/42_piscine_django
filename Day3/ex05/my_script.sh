#!/bin/sh

# Launch with source ./my_script.sh for venv persistence

python3 -m venv django_venv
source django_venv/bin/activate
pip install -r requirements.txt
