import os

# These are development environment variables
# For production on Heroku, set these via: heroku config:set KEY=value

os.environ.setdefault(
    "DATABASE_URL", "postgresql://neondb_owner:npg_HKWVf7p0wCrR@ep-frosty-mode-ag7flo1h.c-2.eu-central-1.aws.neon.tech/those_maker_gift_450025")

os.environ.setdefault(
    "SECRET_KEY", "django-insecure-dev-key-change-in-production")