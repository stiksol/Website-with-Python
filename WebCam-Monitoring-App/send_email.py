import email.utils
import smtplib
import ssl
import os
from email.message import EmailMessage
import imghdr

_image_path = "images_web/1.png"


def send_email(image_path):
    print("Send email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New object was detected!"
    email_message.set_content("Hey, look at this guy!")
    receiver = "ilya.medvedski@gmail.com"

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    host = "smtp.gmail.com"
    port = 587

    username = "10it218@gmail.com"
    # storing password in Windows envs
    password = os.getenv("PASSWORD")

    #with smtplib.SMTP_SSL(host, port, context=context) as server:
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username, receiver, email_message.as_string())
    print("Email has been sent!")
    server.quit()


if __name__ == "__main__":
    send_email(_image_path)
