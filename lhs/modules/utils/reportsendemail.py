import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from flask import current_app

fromEmail = "abuse@yourresonance.com"

def send_Email(user_email,content,subject):
    try:
        message = Mail(
        from_email=fromEmail,
        to_emails=user_email,
        subject=subject,
        html_content=content)
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as err:
        return {"statusCode":500,"message":err},500
