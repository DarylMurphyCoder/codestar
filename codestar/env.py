import os

# These are development environment variables
# For production on Heroku, set these via: heroku config:set KEY=value
# For local development, use SQLite (don't set DATABASE_URL)

os.environ.setdefault(
    "SECRET_KEY", "django-insecure-dev-key-change-in-production")
os.environ.setdefault("DEBUG", "True")