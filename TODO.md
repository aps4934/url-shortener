# URL Shortener Project TODO

## Backend
- [x] Create Flask app (app.py) with URL shortening endpoint
- [x] Implement in-memory storage for URL mappings
- [x] Generate random short codes
- [x] Add redirect endpoint for short URLs

## Frontend
- [x] Create HTML template (templates/index.html) with form and output
- [x] Add CSS styling (static/styles.css)
- [x] Add JavaScript for AJAX submission (static/script.js)

## Integration
- [x] Run the Flask app
- [x] Test URL shortening functionality

## Scalability Enhancements
- [x] Update requirements.txt to include redis
- [x] Create config.py for Redis settings (e.g., host, port, shards)
- [x] Modify app.py to integrate Redis for storage and caching
- [x] Implement sharding logic (e.g., 4 shards based on hash of short_code)
- [x] Add caching for redirect endpoint to reduce database hits
- [x] Install dependencies locally
- [x] Test scalability features locally
- [x] Update README.md with deployment instructions for load balancing (Gunicorn + Nginx)
