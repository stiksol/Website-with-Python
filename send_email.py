import smtplib
import ssl
import os


def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "10it218@gmail.com"
    # storing password in Windows envs
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, user_email, message)
