#!/bin/bash
mkdir -p /root/project/
cd /root/project/
mkdir -p templates
python3 -m venv web

source web/bin/activate

pip install flask
pip install requests

wget -q https://raw.githubusercontent.com/Sandhj/Store/main/app.py

cd templates
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/index.html
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/result.html
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/create.html
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/renew.html
cd
rm setup.sh
