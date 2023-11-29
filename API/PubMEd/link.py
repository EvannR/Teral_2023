import webbrowser
def generate_pubmed_link(pmid):
    base_url = "https://pubmed.ncbi.nlm.nih.gov/"
    pubmed_link = f"{base_url}{pmid}/"
    return pubmed_link

# Exemple d'utilisation avec un PMID fictif (remplacez-le par votre propre PMID)
pmid = "7947353"
link = generate_pubmed_link(pmid)
print("Lien PubMed:", link)
webbrowser.open(link)

