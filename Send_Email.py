import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(subject: str, message: str, email: str):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USERNAME_1")
    password = os.getenv("PASSWORD")
    receiver = email

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())
