#!/bin/bash
mkdir -p /root/project/
cd /root/project/
mkdir -p templates
mkdir -p static
python3 -m venv web

wget -q https://raw.githubusercontent.com/Sandhj/Store/main/app.py

cd templates
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/index.html
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/result.html
cd

cd /root/project/static
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/styles.css

cd
rm setup.sh
