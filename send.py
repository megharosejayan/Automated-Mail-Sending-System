import email, smtplib, ssl


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText






# password = input("Type your password and press enter:")


def mail(sender, passw, receiver_email, body, sub):
    subject = sub
    sender_email = sender
    password = passw
    # Create a multipart message and set headers
    message = MIMEMultipart()
    #message["From"] = "Lean In Tech <megharose15@gmail.com>"
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = sender_email  # Recommended for mass emails (sending one email to multiple recepients) Not our case.

    # Add body to email
    message.attach(MIMEText(body, "plain"))

  
    text = message.as_string()


   
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    print('y')

    print("hey")

if __name__ == "__main__":
    receiver_email = "megharose15@gmail.com"
    body = "This is an email with attachment sent from Python"
    mail(receiver_email, body)
    print("sdf")


