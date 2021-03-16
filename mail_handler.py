import codecs
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from decouple import config

smtp_server: str = config('MAIL_SMTP_SERVER')
port: int = config('MAIL_SMTP_PORT')
sender_email = config('MAIL_USER_EMAIL')
password = config('MAIL_USER_PASSWORD')

context = ssl.create_default_context()


def sendmail(recipe_data, user):
    server = smtplib.SMTP(smtp_server, port)
    listdata = ''

    for data in recipe_data['meals']:
        listdata += \
            '<tr><td style="font-family: sans-serif; font-size: 12px; vertical-align: top; background-color: #3498db; ' \
            'border-radius: 1px; text-align: center;"> <a href="{}" target="_blank" style="display: inline-block; ' \
            'color: #ffffff; background-color: #3498db; border: 1px solid #3498db;border-radius: 5px; box-sizing: ' \
            'border-box; cursor: pointer; text-decoration: none; font-size: 14px; font-weight: bold; margin: 0; ' \
            'padding: 12px 25px; text-transform: capitalize;">{}</a> </td></tr>'.format(data['sourceUrl'],
                                                                                        data['title'])

    try:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        print("start logging in")
        server.login(sender_email, password)
        print("logged in")
        print("Sending Mail")
        print(recipe_data)

        message = MIMEMultipart("alternative")
        message["Subject"] = "Todays recipies"
        message["From"] = sender_email
        message["To"] = user['email']

        html_mail = MIMEText(codecs.open("recipe_email.html").read()
                             .replace("$LISTINPUT", listdata)
                             .replace("$DIET", user['diet'])
                             .replace("$TARGET_CALORIES", str(user['target_calories'])),
                             "html")

        message.attach(html_mail)

        server.sendmail(sender_email, user['email'], message.as_string())
        print("Email sent")
    except Exception as e:
        print(e)
    finally:
        server.quit()
