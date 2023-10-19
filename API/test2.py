import requests

# Remplacez "YOUR_API_KEY" par votre clé d'API Crunchbase
api_key = "17a8290471efc446b35ec95eb53d370a"

# URL de l'API Crunchbase
base_url = "https://api.crunchbase.com/api/v4/"

# Nom de l'entreprise que vous souhaitez rechercher
company_name = "Apple"  # Remplacez ceci par le nom de l'entreprise que vous recherchez

# Effectuer une recherche sur l'entreprise
search_url = f"{base_url}organizations/search?name={company_name}&user_key={api_key}"

response = requests.get(search_url)

print(response.text)