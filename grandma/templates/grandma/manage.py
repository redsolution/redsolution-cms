#!/usr/bin/env python
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([{% for package in grandma_settings.packages.all %}{% if package.ok %}
    r'{{ package.path }}',{% endif %}{% endfor %}
])
sys.path[0:0] = [
    os.path.abspath(current_dir),
    os.path.abspath(os.path.join(current_dir, '..', 'parts', 'django'))
]

from django.core.management import execute_manager
try:
    import settings_{{ hash }} as settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings_{{ hash }}.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)