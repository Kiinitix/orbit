import smtplib
from email.mime.text import MIMEText
from config.settings import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

def send_alert_email(subject, message, recipient="admin@example.com"):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
