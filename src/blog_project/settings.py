import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
ROOT_URLCONF = "blog_project.urls"

INSTALLED_APPS = [
    'apps.users',
    'apps.posts',
    'apps.stories',
    'apps.videos',
]
