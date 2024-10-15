import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(name, email, phone, message):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    sender_email = email
    sender_password = os.getenv('SMTPLIB_PASSWORD')
    destinatario_email = os.getenv('EMAIL')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = destinatario_email
    msg['Subject'] = f"Novo contato de {name}"

    body = f"""
    Nome: {name}
    Email: {email}
    Telefone: {phone}

    Mensagem:
    {message}
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(destinatario_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, destinatario_email, text)
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
