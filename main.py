import csv

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
        nom = row[0]
        age = row[1]
        
        # Vous pouvez maintenant faire ce que vous voulez avec les données
        print(f"Nom : {nom}, Âge : {age}")
        
        #print(row)