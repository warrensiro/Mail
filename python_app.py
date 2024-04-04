from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = os.environ.get('EMAIL_USER')
email_password = os.environ.get("EMAIL_PASS")


email_receiver = 'yetahac537@adstam.com'

subject = "Don't forget to subscribe"

body = """ 
Kindly follow up on this attachment
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())