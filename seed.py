"""
Run once to populate the DB with the initial tasks.
Usage:  python seed.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
django.setup()

from tasks.models import Task  # noqa: E402

INITIAL_TASKS = [
    {'category': 'Personal',  'text': 'Buy grocery',              'completed': False},
    {'category': 'Personal',  'text': 'Visit own shop',           'completed': False},
    {'category': 'Work',      'text': 'Design Login page',        'completed': False},
    {'category': 'Work',      'text': 'Arrange call with client', 'completed': False},
    {'category': 'Academic',  'text': 'Do math homework',         'completed': True},
]

if Task.objects.exists():
    print('Database already has tasks — skipping seed.')
else:
    for t in INITIAL_TASKS:
        Task.objects.create(**t)
    print(f'Seeded {len(INITIAL_TASKS)} tasks.')
