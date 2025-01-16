from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_account():
    # Ambil data dari form
    protocol = request.form['protocol']
    username = request.form['username']
    expired = request.form['expired']

    # Debugging: Log data yang diterima dari form
    print(f"Received data - Protocol: {protocol}, Username: {username}, Expired: {expired}")

    # Menjalankan skrip shell dengan input dari user
    try:
        # Menjalankan skrip shell dengan argumen (bukan input interaktif)
        print(f"Running script for protocol: {protocol} with username: {username} and expired: {expired}")
        
        result = subprocess.run(
            [f"/usr/bin/create_{protocol}", username, expired],  # Argumen username dan expired
            text=True,
            capture_output=True,
            check=True
        )
        
    except subprocess.CalledProcessError as e:
        # Debugging: Tangkap kesalahan dan tampilkan error stderr
        print(f"Error: {e.stderr.strip()}")
        output = f"Error: {e.stderr.strip()}"
    
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
