from pymed import PubMed
import json

# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required 
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="MyTool", email="my@email.address")

# Create a GraphQL query in plain text
def query(query):

# Execute the query against the API
    results = pubmed.query(query, max_results=2)

# Loop over the retrieved articles
    for article in results:


        article = article.toJSON()
        #print(article)

        data = json.loads(article)



        title = data['title']
        id = data['pubmed_id']


        print("id :", id)
        print("titre :", title)
        #
        #print(type(article))

query("ulna implant")

        #article_str = f"{article.toJSON}"

        #with open(article, 'r') as fichier:
        #data = json.loads(article_str)
            # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle)
        #print(type(article))

    # Print a JSON representation of the object
        #print(article.toJSON())