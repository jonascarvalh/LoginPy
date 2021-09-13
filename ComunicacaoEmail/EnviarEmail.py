import smtplib
import email.message
from NumeroAleatorio import GerarNumero

def EnviarEmail():

    numero = GerarNumero()
    corpo = f"""
    Verificação LoginPy
    Seu código de verificação é: {numero}
    Abs
    Equipe LoginPy
    """

    msg = email.message.Message()
    msg['Subject'] = "Confirmação LoginPy"
    msg['From']    = '' # Você precisa criar um e-mail que fará o envio
    password       = '' # Senha desse novo e-mail
    msg['To']      = '' # Destinatário
    msg.add_header('Content=Type', 'text/html')
    msg.set_payload(corpo)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']],msg.as_string().encode('utf-8'))
    
    print('O E-mail de verificação foi enviado!')
    print('Verifique também o spam')
# EnviarEmail