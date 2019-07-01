from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    """
    Function to send emails to new users

    Args:
        Subject:The email's subject
        Template:Where we create the email's body
        To:Recipient of the email
        **Kwargs:Any keyword arguments
    """
    sender_email = 'kibet1816@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)