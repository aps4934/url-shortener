from flask import Flask, request, redirect, jsonify, render_template
import random
import string
import logging
import redis
import hashlib
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, NUM_SHARDS, CACHE_TTL

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Initialize Redis clients for sharding with error handling
redis_clients = []
redis_available = False
for i in range(NUM_SHARDS):
    try:
        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB + i, socket_connect_timeout=1)
        client.ping()  # Test connection
        redis_clients.append(client)
        redis_available = True
        app.logger.info(f"Connected to Redis shard {i} (DB {REDIS_DB + i})")
    except (redis.ConnectionError, redis.TimeoutError):
        app.logger.warning(f"Redis shard {i} not available, falling back to in-memory storage")
        redis_clients.append(None)  # Placeholder for in-memory fallback

# Fallback in-memory storage
url_map = {}

def get_shard(short_code):
    """Determine which shard to use based on hash of short_code."""
    hash_value = int(hashlib.md5(short_code.encode()).hexdigest(), 16)
    return hash_value % NUM_SHARDS

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
    shard = get_shard(short_code)
    client = redis_clients[shard]

    if client:
        # Ensure uniqueness across shards (simplified; in production, check all shards)
        while client.exists(short_code):
            short_code = generate_short_code()
            shard = get_shard(short_code)
            client = redis_clients[shard]
        client.set(short_code, original_url)
    else:
        # Fallback to in-memory
        while short_code in url_map:
            short_code = generate_short_code()
        url_map[short_code] = original_url

    short_url = request.host_url + short_code
    app.logger.debug(f"Generated short URL: {short_url} for original URL: {original_url} on shard {shard}")
    return jsonify({'short_url': short_url})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Check cache first (using shard 0 for cache, or a separate cache instance)
    cache_client = redis_clients[0] if redis_clients[0] else None
    if cache_client:
        cached_url = cache_client.get(f"cache:{short_code}")
        if cached_url:
            app.logger.debug(f"Cache hit for short code {short_code}")
            return redirect(cached_url.decode())

    # Find the shard and get URL
    shard = get_shard(short_code)
    client = redis_clients[shard]
    original_url = None

    if client:
        original_url = client.get(short_code)
        if original_url:
            original_url = original_url.decode()
    else:
        # Fallback to in-memory
        original_url = url_map.get(short_code)

    if original_url:
        # Cache the URL if Redis available
        if cache_client:
            cache_client.setex(f"cache:{short_code}", CACHE_TTL, original_url)
        app.logger.debug(f"Redirecting short code {short_code} to {original_url} from shard {shard}")
        return redirect(original_url)

    app.logger.debug(f"Short code {short_code} not found")
    return jsonify({'error': 'Short URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
