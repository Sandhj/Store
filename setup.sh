#!/bin/bash
mkdir -p /root/project/
cd /root/project/
mkdir -p templates
mkdir -p static
python3 -m venv web

wget -q https://raw.githubusercontent.com/Sandhj/Store/main/app.py

cd templates
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/index.html /root/project/templates/
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/result.html /root/project/templates/
cd

cd /root/project/static
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/styles.css/root/project/static/

cd
rm setup.sh
