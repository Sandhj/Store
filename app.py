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

    # Menjalankan script shell dengan input dari user
    try:
        # Menyesuaikan protokol dan input untuk skrip shell
        result = subprocess.run(
            [f"/usr/bin/create_{protocol}"],  # Menyesuaikan dengan protokol
            input=f"{username}\n{expired}",  # Input yang dikirimkan ke skrip shell
            text=True,
            capture_output=True,
            check=True
        )
        # Hasil output dari script shell
        output = result.stdout.strip()
    except subprocess.CalledProcessError as e:
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
    app.run(host='0.0.0.0', port=5003)
    
