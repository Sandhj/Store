from flask import Flask, render_template, request
import subprocess

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

    # Debugging: Cetak data input yang diterima dari form
    print(f"Received data - Protocol: {protocol}, Username: {username}, Expired: {expired}")

    # Menjalankan script shell dengan input dari user
    try:
        # Debugging: Log sebelum menjalankan skrip shell
        print(f"Running script for protocol: {protocol} with username: {username} and expired: {expired}")
        
        # Menjalankan skrip shell
        result = subprocess.run(
            [f"/usr/bin/create_{protocol}"],  # Menyesuaikan dengan protokol
            input=f"{username}\n{expired}",  # Input yang dikirimkan ke skrip shell
            text=True,
            capture_output=True,
            check=True
        )
        
        # Debugging: Log output dari skrip shell
        print(f"Script output: {result.stdout.strip()}")
        
        # Hasil output dari script shell
        output = result.stdout.strip()

    except subprocess.CalledProcessError as e:
        # Debugging: Tangkap kesalahan dan tampilkan error stderr
        print(f"Error: {e.stderr.strip()}")
        output = f"Error: {e.stderr.strip()}"

    # Render halaman hasil
    return render_template(
        'result.html',
        username=username,
        expired=expired,
        protocol=protocol,
        output=output
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
