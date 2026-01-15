import logging

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from accountg.models import User

from gallery.celeryapp import app

logger = logging.getLogger(__name__)

@app.task
def send_email_task(email, template: str, context: dict) -> bool:
    html_body = render_to_string(template, context)
    msg = EmailMultiAlternatives(subject=context["subject"], to=[email])
    if context.get("reply_to"):
        msg = EmailMultiAlternatives(subject=context["subject"], to=[email], reply_to=[context["reply_to"]])
    msg.attach_alternative(html_body, "text/html")
    msg.send()
    logger.info("Email: {}, Subject: {}".format(email, context["subject"]))
    return True


def send_email(user: User, template:str, context: dict):
    context["username"] = user.username
    return send_email_task.delay(user.email, template, context)
