import os

os.environ.setdefault(
    "DATABASE_URL", "sqlite:///db.sqlite3")
os.environ.setdefault("SECRET_KEY", "django-insecure-local-dev-key-not-for-production")
os.environ.setdefault("DEBUG", "True")