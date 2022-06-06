from celery import shared_task
from crypto_proj.celery import app

from .models import Test
from .utils import get_random_code


@shared_task
def create_test_object(name):
    Test.objects.create(name=name)

@shared_task
def create_all_codes():
    for test in Test.objects.all():
        test.code = get_random_code()
        test.save()

@app.task
def run_create_obj():
    create_test_object.delay(name='new2022')

