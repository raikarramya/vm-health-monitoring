import smtplib
from email.message import EmailMessage
from config import *

def send_alert(message):
    msg = EmailMessage()
    msg["Subject"] = "VM Health Alert"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)
