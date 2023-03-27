#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sends email with Python3 standard library.

import pathlib
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PORT = 465
SMTP_SERVER = input("smtp server: ")
SENDER = input("sender: ")
PASSWORD = input("pwd: ")
RECEIVER = input("receiver: ")
PATH = input("content path: ")


def get_message() -> str:
    message = MIMEMultipart("alternative")

    # Parameters
    message["Subject"] = "mail formatting test"
    message["From"] = SENDER
    message["To"] = RECEIVER

    # Content
    html = MIMEText(pathlib.Path(PATH).read_text(), "html")
    message.attach(html)

    return message.as_string()


if __name__ == "__main__":
    # Communication
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECEIVER, get_message())
