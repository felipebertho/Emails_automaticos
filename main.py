import yagmail
import os
import time

#remetente e destinatário
sender = 'fhbertho@gmail.com'
receiver = 'felipebertho@icloud.com'
#Assunto
subject = "Teste de envio do script"
#Conteudo do e-mail
contents = "Esse é o conteúdo do e-mail"

#configuração da senha do e-mail para utilização do script.
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWD'))

yag.send(to=receiver, subject=subject, contents=contents)

print("E-mail enviado! ")