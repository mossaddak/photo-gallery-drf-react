import logging

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from accountg.models import User

logger = logging.getLogger(__name__)


def send_email(user: User, template:str, context: dict) -> bool:
    html_body = render_to_string(template, context)
    context["user"] = user
    msg = EmailMultiAlternatives(subject=context["subject"], to=[user.email])
    if context.get("reply_to"):
        msg = EmailMultiAlternatives(subject=context["subject"], to=[user.email], reply_to=[context["reply_to"]])
    msg.attach_alternative(html_body, "text/html")
    msg.send()
    logger.info("Email: {}, Subject: {}".format(user.email, context["subject"]))
    return True
