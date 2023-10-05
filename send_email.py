import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = 'iamwellys@gmail.com'
    password = "othivclljwhmhswx"  # generate via gmail
    receiver = 'iamwellys@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=message)

