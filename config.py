import os

# Redis configuration
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

# Sharding configuration
NUM_SHARDS = int(os.getenv('NUM_SHARDS', 4))  # Number of shards

# Cache configuration
CACHE_TTL = int(os.getenv('CACHE_TTL', 3600))  # TTL for cached redirects in seconds (1 hour)
