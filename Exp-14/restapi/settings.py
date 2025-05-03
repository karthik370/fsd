import os
INSTALLED_APPS = [
    'rest_framework','base'
]
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        
    },
]
