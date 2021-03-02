import smtplib, ssl
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "aschvin00@gmail.com"
password = input("Type PW and enter: ")

context = ssl.create_default_context()