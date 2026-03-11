import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("your_email@gmail.com", "password")

message = """
Subject: Security Alert

Your account needs verification.

Click here:
http://localhost:5000
"""

server.sendmail("your_email@gmail.com", "target@email.com", message)