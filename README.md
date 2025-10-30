# Scalable URL Shortener

A high-performance, scalable URL shortener web application built with Python Flask, Redis, and modern web technologies. Designed to handle millions of requests through advanced architecture including data sharding, intelligent caching, and load balancing.

## 🚀 Features

- **High Performance**: Optimized with Redis caching and sharding for lightning-fast redirects
- **Scalable Architecture**: Data sharding across multiple Redis instances for horizontal scaling
- **Intelligent Caching**: Reduces database hits with configurable TTL-based caching
- **Load Balancing Ready**: Supports multiple instances behind load balancers
- **Reliable Storage**: Persistent Redis storage with in-memory fallback
- **Modern Dark UI**: Beautiful, responsive dark mode interface with cyan accents and interactive features
- **Real-time Feedback**: Loading states and copy-to-clipboard functionality
- **Production Ready**: Configurable for cloud deployments

## 🏗️ Architecture

### Backend
- **Flask**: Lightweight web framework
- **Redis**: High-performance data structure store for caching and storage
- **Sharding**: MD5 hash-based distribution across 4 Redis shards
- **Caching**: TTL-based cache for frequently accessed URLs
- **Load Balancing**: Gunicorn workers for concurrent request handling

### Frontend
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Asynchronous operations with loading states and error handling

## ⚙️ Installation (Local Setup)

### Prerequisites

- Python 3.8+
- Redis server (install locally or use a cloud instance like Redis Labs)

### Clone the repository

```bash
git clone https://github.com/aps4934/url-shortener.git
cd url-shortener
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set up Redis

Ensure Redis is running locally on default port 6379, or update `config.py` with your Redis details.

### Run the Flask app

```bash
python app.py
```

Open your browser at 👉 http://localhost:5000

## 🌐 Deployment with Scalability

### Local Testing with Gunicorn

For production-like testing:

```bash
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app
```

### Cloud Deployment (e.g., on Render with Redis)

1. Set up a Redis instance (e.g., on Redis Labs or AWS ElastiCache).
2. Push your code to GitHub (make sure requirements.txt and config.py are included).
3. On Render, create a New Web Service and connect this repo.
4. Set environment variables in Render:
   - `REDIS_HOST`: Your Redis host
   - `REDIS_PORT`: Your Redis port (default 6379)
   - `REDIS_DB`: Starting DB number (default 0)
   - `NUM_SHARDS`: Number of shards (default 4)
   - `CACHE_TTL`: Cache TTL in seconds (default 3600)
5. Use the following settings:

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn --workers 4 --bind 0.0.0.0:$PORT app:app
```

Deploy! 🎉 Your app will be live at `https://<your-app-name>.onrender.com`

### Load Balancing with Nginx

For high availability, deploy multiple instances behind Nginx:

1. Run multiple Gunicorn workers or deploy to multiple servers.
2. Configure Nginx as a reverse proxy and load balancer:

```nginx
upstream app_servers {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    # Add more servers as needed
}

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://app_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

3. Reload Nginx: `sudo nginx -s reload`

## 📂 Project Structure

```
url-shortener/
│
├── app.py               # Flask backend application with Redis integration
├── config.py            # Configuration for Redis and sharding
├── requirements.txt     # Python dependencies
│
├── templates/           # HTML templates
│   └── index.html
│
└── static/              # Frontend static files
    ├── styles.css
    └── script.js
```

## 🔧 Configuration

Edit `config.py` to customize:

- Redis connection details
- Number of shards
- Cache TTL

## 👤 Creator

Created by Aditya Pratap Singh.
Feel free to open issues or submit pull requests for improvements!

## 📜 License

This project is licensed under the MIT License.
