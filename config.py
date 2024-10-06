from os import environ as env
import multiprocessing

# Set port and debug mode from environment variables, with defaults
PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)  # Bind to the specified port
workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes
threads = 2 * multiprocessing.cpu_count()  # Number of threads per worker
