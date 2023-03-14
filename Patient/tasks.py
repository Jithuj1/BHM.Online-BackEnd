from __future__ import absolute_import, unicode_literals
from celery import shared_task
from . import views


@shared_task
def celery_worker(date, dock, patient, email):
    return views.send_email_celery(date, dock, patient, email)


    