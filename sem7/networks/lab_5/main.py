import email, smtplib, ssl

from time import sleep
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = input("input subject: ")
body = input("input msg: ")

receiver_email = input("input receiver's email: ")
sender_email = input("input sender's email: ")
password = input("input pwd: ")

message = MIMEMultipart()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

interval = int(input("input interval: "))

is_filename = input("is there a filename: yes or no: ")

if is_filename == "yes":
    filename = input("input filename: ")
    
    with open(filename, "rb") as attachment:
        file = MIMEBase("application", "octet-stream")
        file.set_payload(attachment.read())

    encoders.encode_base64(file)

    file.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(file)

text = message.as_string()

context = ssl.create_default_context()

counter = 0

print("to stop use keyboard interrupt (ctrl+c)")

while True:
    counter += 1
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        print("successfully delivered " + str(counter) + " message(s)")

    sleep(interval)

