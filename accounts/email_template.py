import smtplib,  email.message
from app.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
import random
from accounts.models import AcontUser
from django.contrib.auth.hashers import make_password



def send_email(assunto, body_message ,to_message=any):

    message = email.message.Message()
    message["Subject"] = assunto
    message["From"] = EMAIL_HOST_USER
    message["To"] = to_message
    password = EMAIL_HOST_PASSWORD
    message.add_header('Content-Type', 'text/html')
    message.set_payload(body_message)
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(message["From"], password)
    # sending the mail
    s.sendmail(message["From"], message["To"], message.as_string().encode('utf-8'))
    # terminating the session
    s.quit()

    print('email enviado para:' , message["To"] )


def reset_senha(email_destino, senha ):
    assunto= " RESET DE SENHA   -- GESTAOTI--"

        
    corpo_email = f"""
            <h1> Foi realizado o reset de senha com sucesso. </h1> 
            <p>Para acessar o sistema --GESTAOTI--, segue abaixo sua nova senha de acesso. </p>
            <h2> {senha} </h2>      
            """
    
    try: 

        send_email(assunto,corpo_email,email_destino)

    except:
        ...




def solicitacao_folga(instance):
    assunto = "Nova solicitação de folga - GestãoTI"

    corpo_email= f"""
            <h1> Uma nova solicitação de folga foi incluida para sua aprovação. </h1> 
            <p> Solicitado por: <strong>{instance.folga_pessoa}</strong>.  </p>
            <p> Data solicitada: <strong>{instance.day}</strong>.</p>
            <p> Motivo da solicitação: <strong>{instance.motivo}</strong>.</p>
            <p> Unidade: <strong>{instance.unit}</strong>.</p>
            <p> Observação: <strong>{instance.observacao}</strong>.</p>

            """
        
    email_gestao= AcontUser.objects.filter(cargo_id = 1).values('email')

    emails = []
    if email_gestao.count() > 1:
        for i in range(email_gestao.count()):
            emails = email_gestao[i]['email']
            try: 
                send_email(assunto,corpo_email,emails)
            except:
                ...

    else:
        emails = email_gestao[0]['email']
        try: 
            send_email(assunto,corpo_email,emails)

        except:
            ...





def aprovacao_folga(instance):
        assunto = "Folga incluida no seu roteiro - GestãoTI"

        corpo_email= f"""
            <h1> Uma folga foi aprovada e adicionada em seu roteiro. </h1> 
            <p> Data da Folga: <strong>{instance.day}</strong>.</p>
            <p> Unidade: <strong>{instance.unit}</strong>.</p>
            <p> Data da aprovação <strong>{instance.date_updated}</strong>.</p>

            """
        email_volantes = AcontUser.objects.filter(cargo_id = 3).values('email')

        emails= []
        if email_volantes.count() > 1:
            for i in range(email_volantes.count()):
                emails = email_volantes[i]['email']
                try:
                    send_email(assunto,corpo_email,emails)
                except:
                    ...
        else:
            emails = email_volantes[0]['email']
            try: 
                send_email(assunto,corpo_email,emails)

            except:
                ...


