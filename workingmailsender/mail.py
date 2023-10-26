
#motdepasse = 'rhdd ywyi bebf qptd' # Evann's token 
password = "qxqe cfaz ivxp wncb" #David's token 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from mail_text import text


#################
# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_address = 'David@teral.com.co'
email_password = password

# on rentre les informations sur le destinataire
email_receiver = 'evann@teral.com.co'
name = "Evann"

pdf_link = "https://mail-attachment.googleusercontent.com/attachment/u/1/?ui=2&ik=845860c20e&attid=0.1&permmsgid=msg-f:1779852518580841329&th=18b34e6f82986b71&view=att&disp=inline&realattid=cdeecb1f86cdad3e_0.1&saddbat=ANGjdJ9GwQtOkjZwMlv6Y-Xe1Yu8nMSJkPVnpEdpgCMnmoyJ3DchEzd_pQaqxpSrRIPJOeZpHHDDz_f9p6As8ZMPYGieQFfyWLSuWQDMSDmBGtRVirsRHr8X5pfDXdIrwmCJnlUYEKvoQIZq0bwWmxnY1WjGMPf48k2Y-Kkutx6h9GFW1bHeUd70dxWWDHr-8cDxZRb3dKXq8Wff1umP_GeRjM0GSd_0D7jXQ935Do7N90svGGk5rj9CwvycHVpl-NXwyv8aE_ykNykF0KNy261bnLEB7nawcC6SC5ANNWwJWqF9a70-jD2Oj3fjMUEulqqKl0sP-1LO4W57xRjEFvBruhLVokh2zl5yU7NrZuL0IYIMudrA4I7KLnMqRwOIL3S5PYiPtfkWu5O5JMYID8a2IjseVWuaIJY_sU5t8RKvpwzF0EmDQqWW1voqW7vfFKFPMUHiIeC5qtVtoCnT5fk4iMQzsx-EsDGDztO4KkLPRcnjQPusBXVhcOkDBW7hkoVP3XFIxOIaMSx3l0kBqd4j48CNpn05Cx_uasH4Q7QjkFAaDuN8qLjLrBEXREYRW0r-3LYJyDp6Hi_9MkjHSxK8N9ODhZ9dTjpHtnddv0vVGmXXxmcBWeEKlloCeOcIxQ_ciIkgzpltEwRW4Gxi-CHIjOW19Exmx81Hmgdg8wTEd67Zj-K12Wc58xj6w5jDeiilL6zu_5re8dlMYCuO27xKnqHb3pPAHOeyTkgBgfDZ35bH-SJbZOHuExVlgkefqA9zV-U6WkSDaqx9j-whA3AfGR9jheIpquTQiIVexqdXLJTCzhV865e2i3ZPOzlhMtW_6_seywxEZErWZn0ixcTfWqAQph0Te95fJM7mk6llqjoRumPx62nPv8w-7k-j6C5Gx5nN7opWB1-c9ZMVBEo1Rnwgc9l58LGBgRdIHP2VvR6W7bYq9Wq5vQOXkzEH37xgjO9Me2xS6RxBsQrYFSXshKZLttqLnb62_1bKZky6bXX5xJzEk1iZOI71qPkL9OcgaLHbRUBJdSY5XekrnyouFWW0v7qukB0c7c8eobF8_Jkf2bc1CkkInvIZqBqmTRwfQefLiQuE5kvZZd3M"


def send_mail(name,adresse,version) :
# on crée un e-mail
    message = MIMEMultipart("alternative")
    message["Subject"] = "Teral : Revolutionize Healthcare Networking with Our App"
    message["From"] = email_address
    message["To"] = email_receiver

    body = text(name,version,pdf_link)

    html_mime = MIMEText(body, 'html')
    message.attach(html_mime)

# on crée la connexion
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
        server.login(email_address, email_password)
  # envoi du mail
        server.sendmail(email_address, adresse, message.as_string())
        return(version)

#send_mail(name, email_receiver,2)