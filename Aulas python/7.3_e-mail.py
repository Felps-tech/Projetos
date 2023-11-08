# Não funciona porque o Google desativou esse módulo
import smtplib, ssl, email.message

setor = 'B'
msg = email.message.Message() 
msg['Subject'] = f'Planilha Financeira: {setor}'

body = 'Bom dia felps'

msg['From'] = 'aaaaa@gmail.com'
msg['To'] = 'bbbb@gmail.com'
password = 'cccccccc'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)

context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg['From'], password)
    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    conexao.quit()