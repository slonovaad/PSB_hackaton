import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_mail(mail: str, subject: str, text: str, *args: str):
    """Функция, отправляющая письмо на почту"""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "hacatontest@gmail.com"
    password = "izgu gpfq ipzq orkt"

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = mail
    msg['Subject'] = subject

    body = text
    msg.attach(MIMEText(body, 'plain'))
    try:
        for item in args:
            filename = item
            attachment = open(filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")
            msg.attach(part)
    except:

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(username, mail, text)
        server.quit()
    except Exception as e:
        print(f"Ошибка: {e}")

send_mail("hacatontest@gmail.com", "test", "text in body", "file.txt", "file2.txt")