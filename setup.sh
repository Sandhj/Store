#!/bin/bash
mkdir -p /root/project/
cd /root/project/
mkdir -p templates
mkdir -p static
python3 -m venv web

wget -q https://raw.githubusercontent.com/Sandhj/Store/main/app.py
wget -q -P https://raw.githubusercontent.com/Sandhj/Store/main/index.html /root/project/templates/
wget -q -P https://raw.githubusercontent.com/Sandhj/Store/main/result.html /root/project/templates/
wget -q -P https://raw.githubusercontent.com/Sandhj/Store/main/styles.css/root/project/static/

rm setup.sh
