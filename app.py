from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    """Serve the index.html file."""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files."""
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)