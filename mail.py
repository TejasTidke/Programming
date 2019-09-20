import smtplib
import os
from email.header import Header
from email.utils import formataddr

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()  #identifies ourselves with the mail server that we are using
    smtp.starttls() #to encrypt the traffic
    smtp.ehlo() #to re-identify ourselves as encrypted connection

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Regarding your text role"
    body = "This is to inform u that ur text role has been updated"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(formataddr((str(Header('Someone Somewhere', 'utf-8')), EMAIL_ADDRESS)),'tejas_tidke@persistent.com', msg)
