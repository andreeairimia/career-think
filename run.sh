#!/usr/bin/env bash
python3 -m virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
cd app
python3 app.py
