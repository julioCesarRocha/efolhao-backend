import os
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Producao")

BASE_DIR = Path(__file__).resolve().parent.parent

# Obtém o caminho absoluto para o arquivo de banco de dados
db_path = os.path.join(BASE_DIR, 'db.sqlite3')

# Define a variável de ambiente DATABASE_URL
os.environ.setdefault("DATABASE_URL", f"sqlite:///{db_path}")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': db_path,
    }
}

os.environ.setdefault("SECRET_KEY", "django-insecure-a#7-yhzrp^^+^irsvj^2d(9q58#+5ucj$r(hryg8($#_!)0zq(")
