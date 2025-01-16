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

# Menentukan path ke project dan venv
PROJECT_DIR="/root/project/web"
VENV_DIR="$PROJECT_DIR/venv"
APP_FILE="$PROJECT_DIR/app.py"
SERVICE_NAME="webapp.service"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"

# Mengecek apakah direktori project dan venv ada
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Direktori project tidak ditemukan: $PROJECT_DIR"
  exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment tidak ditemukan: $VENV_DIR"
  exit 1
fi

if [ ! -f "$APP_FILE" ]; then
  echo "File aplikasi tidak ditemukan: $APP_FILE"
  exit 1
fi

# Membuat file service systemd
echo "Membuat file service systemd..."

cat <<EOL > $SERVICE_FILE
[Unit]
Description=Web App
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$PROJECT_DIR
ExecStart=$VENV_DIR/bin/python $APP_FILE
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd untuk membaca file service baru
echo "Reload systemd daemon..."
sudo systemctl daemon-reload

# Enable dan start service
echo "Menjalankan dan mengaktifkan service..."
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

# Cek status service
echo "Cek status service..."
sudo systemctl status $SERVICE_NAME

cd
rm setup.sh
