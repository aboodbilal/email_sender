from email.message import EmailMessage 
import ssl
import smtplib
import time

email_sender="hashlamonabdalrahman@gmail.com"
email_password="fpbq iypc myve qvjh"

email_receiver="dalahhashlamoon@gmail.com"

subject="hello "
body="""
hello dalal how r u
"""

em=EmailMessage()
em["From"]=email_sender
em["to"]=email_receiver
em["subject"]= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
