import smtplib
import os
from email.message import EmailMessage
import mimetypes


def generate_email(_from, to, subject, body, attachment):
    msg = EmailMessage()
    msg["From"] = _from
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment is not None:
        mime_guess, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_guess.split(r'/',1)
        with open(attachment, 'rb') as a:
            msg.add_attachment(a.read(), 
                maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment))
        

    return msg

def send_email(email, username, password):
    mail_server = smtplib.SMTP("localhost")
    #mail_server = smtplib.SMTP_SSL('smtp.example.com')
    mail_server.login(username, password)
    mail_server.send_message(email)
    mail_server.quit()



    


