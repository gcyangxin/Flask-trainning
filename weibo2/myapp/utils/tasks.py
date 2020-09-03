from myapp.extensions import  celery,mail
from flask_mail import Message



@celery.task
def send_async_email(subject,recipients,body):
    message=Message(subject=subject,recipients=[recipients],body=body)
    mail.send(message)


