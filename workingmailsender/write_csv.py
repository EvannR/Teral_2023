import csv
def add_element(name, mail_address,version):
# Ouvrir le fichier CSV en mode d'écriture (ou création s'il n'existe pas)
    with open('mail_envoye.csv', 'a', newline='') as csv_file:
    # Créer un objet writer
        writer = csv.writer(csv_file)
        writer = csv.writer(csv_file, delimiter=';')
    
    # Créer une liste représentant la nouvelle ligne que vous souhaitez ajouter
        nouvelle_ligne = [name, mail_address, version]
    
    # Écrire la nouvelle ligne dans le fichier CSV
        writer.writerow(nouvelle_ligne)
        csv_file.close()

#add_element("bla","bla",2)