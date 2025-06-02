#!/bin/bash

python3 -m venv my-venv

source my-venv/bin/activate

pip install --upgrade pip
pip install -r src/requirements.txt
