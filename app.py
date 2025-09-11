from flask import Flask, request, redirect, jsonify, render_template
import random
import string
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

url_map = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        app.logger.debug("No URL provided in request")
        return jsonify({'error': 'No URL provided'}), 400

    short_code = generate_short_code()
    while short_code in url_map:
        short_code = generate_short_code()

    url_map[short_code] = original_url
    short_url = request.host_url + short_code
    app.logger.debug(f"Generated short URL: {short_url} for original URL: {original_url}")
    return jsonify({'short_url': short_url})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    if short_code in url_map:
        app.logger.debug(f"Redirecting short code {short_code} to {url_map[short_code]}")
        return redirect(url_map[short_code])
    app.logger.debug(f"Short code {short_code} not found")
    return jsonify({'error': 'Short URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
