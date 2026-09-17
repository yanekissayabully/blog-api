from pathlib import Path

from decouple import Config, RepositoryEnv

BASE_DIR: Path = Path(__file__).resolve().parent.parent
SETTINGS_DIR: Path = Path(__file__).resolve().parent
ENV_FILE: Path = SETTINGS_DIR / '.env'

config = Config(RepositoryEnv(str(ENV_FILE)))

ENV_ID: str = config('BLOG_ENV_ID', default='local')

SECRET_KEY: str = config('BLOG_SECRET_KEY')
DEBUG: bool = config('BLOG_DEBUG', default=False, cast=bool)
ALLOWED_HOSTS: list[str] = config(
    'BLOG_ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=lambda v: [h.strip() for h in v.split(',') if h.strip()]
)

DB_NAME: str = config('BLOG_DB_NAME', default='blog_db')
DB_USER: str = config('BLOG_DB_USER', default='blog_user')
DB_PASSWORD: str = config('BLOG_DB_PASSWORD', default='')
DB_HOST: str = config('BLOG_DB_HOST', default='localhost')
DB_PORT: str = config('BLOG_DB_PORT', default='5432')

JWT_ACCESS_LIFETIME_MINUTES: int = config('BLOG_JWT_ACCESS_LIFETIME_MINUTES', default=15, cast=int)
JWT_REFRESH_LIFETIME_DAYS: int = config('BLOG_JWT_REFRESH_LIFETIME_DAYS', default=7, cast=int)

STATIC_URL: str = config('BLOG_STATIC_URL', default='static/')
MEDIA_URL: str = config('BLOG_MEDIA_URL', default='media/')
