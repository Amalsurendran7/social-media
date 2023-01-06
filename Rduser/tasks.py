from celery.app import task
from celery.utils.log import get_task_logger
from .Email import send_email
from celery import shared_task

logger=get_task_logger(__name__)
@shared_task(name="send_email_task")
def send_email_task(email,username):
    logger.info("send email")
    return send_email(email,username)
    


