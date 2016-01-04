"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import smtplib

class Contacts(Controller):
    def __init__(self, action):
        super(Contacts, self).__init__(action)

    def index(self):    
        #store form information
        formName = request.form['name']
        formEmail = request.form['sender']
        formMessage = request.form['message']

        #setup email server
        server = smtplib.SMTP('smtp.sparkpostmail.com', 2525)
        server.set_debuglevel(1)
        server.starttls()

        # You will need an API Key with 'Send via SMTP' permissions.
        # Create one here: https://app.sparkpost.com/account/credentials
        server.login('SMTP_Injection', 'eada6b6ea29636d0e4e416e554e7b232f8848cd9')

        # sparkpostbox.com is a sending domain used for testing
        # purposes and is limited to 50 messages per account.
        # Visit https://app.sparkpost.com/account/sending-domains
        # to register and verify your own sending domain.
        FROMADDR = 'testing@sparkpostbox.com'
        TOADDRS = ['him@gurselgroup.com','contact@arifgursel.com','arif@vibeheavy.com']
        TO = ", ".join(TOADDRS)
        SUBJECT = 'Message From GBAM Website'
        MESSAGE = 'Name: {}\r\nEmail: {}\r\nMessage:\r\n{}'.format(formName,formEmail,formMessage)
        msg = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}".format(FROMADDR, TO, SUBJECT, MESSAGE)
        server.sendmail(FROMADDR, TOADDRS, msg)
        server.quit()
        
        return redirect('/blog')