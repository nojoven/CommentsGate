import os

# DEPLOYMENT
SERVICE_PORT = os.environ.get("SERVICE_PORT")

# External APIs
LANG_DETECTION_API_KEY = os.environ.get("LANG_DETECTION_API_KEY")
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY")

# Databases
DB_ENGINE = os.environ.get("DB_ENGINE")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

# Docker Hub
DOCKER_USERNAME = os.environ.get("DOCKER_USERNAME")
DOCKER_PASSWORD = os.environ.get("DOCKER_PASSWORD")

# DB URL USED BY THE ORM - When Using DOCKER COMPOSE
SQLALCHEMY_DATABASE_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# DB URL USED BY ORM When using DOCKER ONLY
# SQLALCHEMY_DATABASE_URL = f"{DB_ENGINE}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@host.docker.internal/{DB_NAME}"