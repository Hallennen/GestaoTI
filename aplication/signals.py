from django.db.models.signals import post_save
from aplication.models import Folga, AcontUser
from django.dispatch import receiver
from django.core.mail import send_mail
import smtplib,  email.message
from app.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

@receiver(post_save,sender=Folga)
def post_save(sender,instance,**kargs):

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
    if email_gestao.count() > 0:
        for i in range(email_gestao.count()):
            emails = email_gestao[i]['email']
            send_email(corpo_email,emails)
    else:
        emails = email_gestao[0]['email']
        try: 
            send_email(corpo_email)

        except:
            ...

    
    return  



def send_email(body_message,to_message=any):
        corpo_email= body_message

        message = email.message.Message()
        message["Subject"] = "Nova solicitação de folga - GestãoTI"
        message["From"] = EMAIL_HOST_USER
        message["To"] = "hallennen.marinho3@gmail.com"
        password = EMAIL_HOST_PASSWORD
        message.add_header('Content-Type', 'text/html')
        message.set_payload(corpo_email)
        
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
