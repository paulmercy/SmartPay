import gevent.monkey
gevent.monkey.patch_all()

bind = '0.0.0.0:8000'

# SSL configuration
# certfile = 'certificate.pem'
# keyfile = 'privatekey.pem'

# # Specify SSL options
# ssl_version = 5  # Use TLS v1.3
# ciphers = 'ECDHE+AESGCM'
# ssl_prefer_server_ciphers = 'off'

# Set the number of Gunicorn workers
workers = 2

# Other Gunicorn settings
timeout = 60
max_requests = 1000
graceful_timeout = 20
accesslog = '-'
errorlog = '-'
worker_class = 'gevent'
