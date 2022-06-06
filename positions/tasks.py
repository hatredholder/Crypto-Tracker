from celery import shared_task
from crypto_proj.celery import app

from .models import Test


@shared_task
def create_test_object(name):
    Test.objects.create(name=name)

@app.task(run_every=1)
def run_create_obj():
    create_test_object.delay(name='new2022')

