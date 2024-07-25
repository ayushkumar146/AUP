# gunicorn.conf.py

import os

bind = "0.0.0.0:8000"  # The address and port on which Gunicorn will listen
workers =3  # Number of worker processes
threads = 2  # Number of threads per worker
worker_class = 'sync'  # The type of workers to use ('sync', 'gevent', etc.)
timeout = 30  # Workers silent for more than this many seconds are killed and restarted
loglevel = 'info'  # The granularity of error log outputs
accesslog = '-'  # The Access log file to write to (use '-' to log to stdout)
errorlog = '-'  # The Error log file to write to (use '-' to log to stderr)

# You can also add more settings if needed, such as:
# preload_app = True  # Preload application before forking workers for faster startup
# max_requests = 1000  # Restart workers after handling this many requests (for robustness)
