# share settings file for djtools

import os.path

# your local environment
LOCAL_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOCAL_MEDIA_DIR = os.path.join(LOCAL_PROJECT_ROOT, 'media')

# SSH production environment
SSH_USER = 'user'
SSH_HOST = 'ssh-host'
SSH_PROJECT_DIR = '/data/stor/www/olimpiadapyth/olimpiada.pyth.hint.pl/www/'
SSH_MEDIA_DIR = SSH_PROJECT_DIR + 'media'
