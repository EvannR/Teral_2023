import webbrowser
import requests

KEY = "17a8290471efc446b35ec95eb53d370a"

#url = "https://www.crunchbase.com"  # Remplacez ceci par l'URL que vous souhaitez ouvrir
url = "https://api.crunchbase.com/api/v4/entities/organizations/tesla-motors?card_ids=founders,raised_funding_rounds&field_ids=categories,short_description,rank_org_company,founded_on,website,facebook,created_at&user_key=" + KEY
webbrowser.open(url)



# Envoi d'une requête GET à l'API
response = requests.get(url)

# Vérification de la réponse de l'API
if response.status_code == 200:
    # La requête a réussi
    #data = response.json() 
    print( response.text) # renvoi tout le contenu de la page sans l'ouvrir
    # Traitez les données ici
else:
    # La requête a échoué
    print(f"Échec de la requête avec le code d'état {response.status_code}")