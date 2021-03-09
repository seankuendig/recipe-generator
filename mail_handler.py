import smtplib, ssl
from decouple import config
from email.message import EmailMessage

smtp_server: str = config('MAIL_SMTP_SERVER')
port: int = config('MAIL_SMTP_PORT')
sender_email = config('MAIL_USER_EMAIL')
password = config('MAIL_USER_PASSWORD')

context = ssl.create_default_context()
server = smtplib.SMTP(smtp_server, port)


def sendmail(recipe_data):
    try:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        print("start logging in")
        server.login(sender_email, password)
        print("logged in")
        print("Sending Mail")
        server.sendmail(sender_email, "aschvin00@gmail.com", recipe_data)
        print("Email sent")
    except Exception as e:
        print(e)
    finally:
        server.quit()
