import uuid
from django.core.mail import send_mail

def send_email(email,username):

    subject = 'Email verification'
    myuuid = uuid.uuid4()
    print(email)
    
    message = "http://127.0.0.1:3000/thank/"+str(myuuid)+"/"+username
    email_from = 'amal76735@gmail.com'
    
    recipient_list=[email]
    
    send_mail( subject, message, email_from ,recipient_list)


