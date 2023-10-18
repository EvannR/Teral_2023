import csv
from mail import send_mail

file_path = 'C:/Users/Evann/OneDrive/Bureau/teral/inversionistas/test.csv'

# Ouvrir le fichier CSV en mode lecture
with open(file_path, 'r', newline='') as csvfile:
    # Créer un lecteur CSV
    csvreader = csv.reader(csvfile)
    csvreader = csv.reader(csvfile, delimiter=';')
    
    # Parcourir chaque ligne du CSV
    for row in csvreader:
        # row est une liste représentant une ligne du CSV
        # Vous pouvez accéder à chaque élément en utilisant l'indice
        name = row[0]
        mail_adress = row[1]
        
        # maintenant fais ce que tu veux avec les données
        print(f"name : {name}, mail : {mail_adress}")
        send_mail(name,mail_adress)
        

