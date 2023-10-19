import csv

# Ouvrir le fichier CSV en mode d'écriture (ou création s'il n'existe pas)
with open('mon_fichier.csv', 'a', newline='') as fichier_csv:
    # Créer un objet writer
    writer = csv.writer(fichier_csv)
    
    # Créer une liste représentant la nouvelle ligne que vous souhaitez ajouter
    nouvelle_ligne = ['Nouvel élément 1', 'Nouvel élément 2', 'Nouvel élément 3']
    
    # Écrire la nouvelle ligne dans le fichier CSV
    writer.writerow(nouvelle_ligne)

# Assurez-vous de bien fermer le fichier après avoir terminé l'opération
fichier_csv.close()