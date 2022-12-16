from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crypto_proj.settings")

app = Celery("crypto_proj")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Beat schedule conf
app.conf.beat_schedule = {
    # Set to update every 50 seconds cuz
    # the task in tasks.py itself
    # takes about ~10 seconds
    "get-crypto-data-every-50-seconds": {
        "task": "positions.tasks.get_crypto_data",
        "schedule": 50.0,
    },
}
