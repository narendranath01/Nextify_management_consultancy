# Django settings for Nextify project.
# This is a test comment for Git

import os
from pathlib import Path


# 1. Standard Django definition
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Force an absolute path string to the root folder
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) # Nextify/Nextify folder
SITE_ROOT = os.path.dirname(PROJECT_ROOT)                  # Actual project root folder

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # This covers all bases: path objects, relative joins, and explicit server roots
            BASE_DIR / 'templates',
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(SITE_ROOT, 'templates'), 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Ensure this path is correct
    }
}

# 1. Ensure WhiteNoise is right under SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- Make sure this is here!
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]

# 2. Add this at the bottom of settings.py for caching static assets
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
