import os
import csv

# Spécifiez le chemin du dossier contenant les sous-dossiers
dossier_parent = "C:\\Users\\Evann\\OneDrive\\Bureau\\teral\\casmedecins\\testdossier"

# Créez un fichier CSV pour enregistrer les noms des dossiers
fichier_csv = "noms_des_dossiers.csv"

# Créez un fichier CSV et écrivez les noms de dossier dans le fichier
with open(fichier_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nom du Dossier"])  # Écrivez l'en-tête de la colonne

    # Parcourez tous les sous-dossiers dans le dossier parent
    for dossier in os.listdir(dossier_parent):
        chemin_dossier = os.path.join(dossier_parent, dossier)
        
        # Vérifiez si le chemin est un dossier
        if os.path.isdir(chemin_dossier):
            writer.writerow([dossier])  # Écrivez le nom du dossier dans le fichier CSV
