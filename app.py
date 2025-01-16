from flask import Flask, render_template, request
import subprocess
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        return render_template('create.html')  # Menggunakan create.html untuk form
    elif request.method == 'POST':
    # Ambil data dari form
    protocol = request.form['protocol']
    username = request.form['username']
    expired = request.form['expired']

    # Debugging: Log data yang diterima dari form
    print(f"Received data - Protocol: {protocol}, Username: {username}, Expired: {expired}")

    # Menjalankan skrip shell dengan input dari user
    try:
        # Debugging: Log sebelum menjalankan skrip shell
        print(f"Running script for protocol: {protocol} with username: {username} and expired: {expired}")

        # Menjalankan skrip shell dengan memberikan input interaktif (username dan expired)
        result = subprocess.run(
            [f"/usr/bin/create_{protocol}"],  # Skrip untuk protokol (vmess, vless, trojan)
            input=f"{username}\n{expired}\n",  # Memberikan input username dan expired
            text=True,
            capture_output=True,
            check=True
        )
        
        # Jika berhasil, outputnya akan ditangkap oleh result.stdout
        print(f"Script output: {result.stdout.strip()}")
        
        # Kirim notifikasi ke bot Telegram admin
        telegram_token = "7360190308:AAH79nXyUiU4TRscBtYRLg14WVNfi1q1T1M"
        chat_id = "576495165"
        message = f"""
        <b>New Account Created</b>
        <b>Protocol:</b> {protocol}
        <b>Username:</b> {username}
        <b>Expired:</b> {expired} days
        """
        send_telegram_notification(telegram_token, chat_id, message)
        
    except subprocess.CalledProcessError as e:
        # Tangkap kesalahan jika terjadi error pada eksekusi skrip shell
        print(f"Error: {e.stderr.strip()}")
        output = f"Error: {e.stderr.strip()}"
        return render_template(
            'result.html',
            username=username,
            expired=expired,
            protocol=protocol,
            output=output
        )

    # Membaca file output yang dihasilkan oleh skrip shell
    output_file = f"/root/project/{username}_output.txt"
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            output = file.read()

        # Menghapus file output setelah dibaca
        os.remove(output_file)

    # Render halaman hasil
    return render_template(
        'result.html',
        username=username,
        expired=expired,
        protocol=protocol,
        output=output
    )
    
def send_telegram_notification(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
