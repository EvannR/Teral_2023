motdepasse = 'rhdd ywyi bebf qptd'
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl


#################
# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_address = 'evannrabeau@gmail.com'
email_password = motdepasse

# on rentre les informations sur le destinataire
email_receiver = 'evann@teral.com.co'

name = "Evann"

# on crée la connexion
#context = ssl.create_default_context()
#with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
  #server.login(email_address, email_password)
  # envoi du mail
  #server.sendmail(email_address, email_receiver, 'bla bla')
#################

def send_mail(name, adresse) :
# on crée un e-mail
    message = MIMEMultipart("alternative")
    message["Subject"] = "[DataScientest] e-mail essai"
    message["From"] = email_address
    message["To"] = email_receiver


# on crée un texte et sa version HTML
    texte = '''
    Bonjour 
    Ma super newsletter
    Cdt

    mon_lien_incroyable
    '''

    html = f'''
    <html>
    <body>
    <h1>Bonjour {name}</h1>
    <p>Ma super newsletter</p>
    <b>Cdt</b>
    <br>
    <a href="https://datascientest.com">mon_lien_incroyable</a>
    </body>
    </html>
    '''

# on crée deux éléments MIMEText, me renseigner à quoi ça sert  
    texte_mime = MIMEText(texte, 'plain')
    html_mime = MIMEText(html, 'html')

# on attache ces deux éléments 
    message.attach(texte_mime)
    message.attach(html_mime)

# on crée la connexion
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
        server.login(email_address, email_password)
  # envoi du mail
        server.sendmail(email_address, adresse, message.as_string())

send_mail(name, email_receiver)