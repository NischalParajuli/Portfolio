import os
import sys
import django
from django.core.management import execute_from_command_line

# Add the project directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Setup Django
django.setup()

# Run migrations
execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])

# Collect static files
execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])