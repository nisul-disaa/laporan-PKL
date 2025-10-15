from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pendahuluan')
def pendahuluan():
    return render_template('pendahuluan.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

@app.route('/kompetensi')
def kompetensi():
    return render_template('kompetensi.html')

@app.route('/kesan')
def kesan():
    return render_template('kesan.html')

@app.route('/dokumentasi')
def dokumentasi():
    return render_template('dokumentasi.html')


if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))  # Railway kasih PORT
    app.run(host='0.0.0.0', port=port)

