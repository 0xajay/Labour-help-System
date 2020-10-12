import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from flask import current_app

fromEmail = "info@yourresonance.com"

def send_Email(user_email,content,subject):
    try:
        message = Mail(
        from_email=fromEmail,
        to_emails=user_email,
        subject=subject,
        html_content=content)
        # with current_app.open_resource('static/r1.png') as f:
        #     image1 = f.read()
        # with current_app.open_resource('static/r2.png') as f:
        #     image2 = f.read()
        # encoded_image1 = base64.b64encode(image1).decode()
        # encoded_image2 = base64.b64encode(image2).decode()
        # attachment = Attachment()
        # attachment.file_content = FileContent(encoded_image1)
        # attachment.file_type = FileType('image/png')
        # attachment.file_name = FileName('image1.png')
        # attachment.disposition = Disposition('inline')
        # attachment.content_id = ContentId('image1')
        # attachment1 = Attachment()
        # attachment1.file_content = FileContent(encoded_image2)
        # attachment1.file_type = FileType('image/png')
        # attachment1.file_name = FileName('image2.png')
        # attachment1.disposition = Disposition('inline')
        # attachment1.content_id = ContentId('image2')
        # message.attachment = attachment
        # message.attachment = attachment1
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as err:
        return {"statusCode":500,"message":err},500
