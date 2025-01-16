#!/bin/bash
mkdir -p /root/project/
cd /roo/project
mkdir -p templates
mkdir -p static

wget -q https://raw.githubusercontent.com/Sandhj/Store/main/app.py /root/project/
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/index.html /root/project/templates/
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/result.html /root/project/templates
wget -q https://raw.githubusercontent.com/Sandhj/Store/main/styles.css/root/project/static
