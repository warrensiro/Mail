import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Attachment follow up'
    body = 'Kindly check the attachment sent on the previous email'

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
