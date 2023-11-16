import openai
from openai.types import Completion, CompletionChoice, CompletionUsage

# Assurez-vous de définir votre clé d'API OpenAI
openai.api_key = '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'

def extract_keywords(article_text):
    # Appel à l'API OpenAI GPT-3.5 pour générer les mots clés
    response = openai.chat.completions.create(
        #model="gpt-3.5-turbo",
        model="Chat",
        messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
    )

    # Récupération de la réponse de l'API
    generated_text = response.choices[0].text.strip()

    # Affichage des mots clés générésop
    print("Mots clés générés :")
    print(generated_text)

    # Vous pouvez également retourner les mots clés sous forme de liste si vous en avez besoin pour votre base de données
    return generated_text.split()

# Remplacez le texte suivant par le texte complet de votre article
article_text = """
Prothèse isoélastique de resurfaçage du radius distal : à
propos d’une série de 24 cas de fractures revues à plus
de 2 ans
Antoine Martins, Priscille Lazarus, Sybille Facca, Stéphanie Gouzou, Nicolas
Meyer, Philippe Liverneaux
To cite this version:
Antoine Martins, Priscille Lazarus, Sybille Facca, Stéphanie Gouzou, Nicolas Meyer, et al.. Prothèse
isoélastique de resurfaçage du radius distal : à propos d’une série de 24 cas de fractures revues à
plus de 2 ans. Revue de Chirurgie Orthopédique et Traumatologique, 2020, 106, pp.1028 - 1033.
ff10.1016/j.rcot.2020.10.020ff. ffhal-03493629ff
1
Mémoire original
Prothèse isoélastique de resurfaçage du radius distal : à propos d’une série de 24 cas de
fractures revues à plus de 2 ans
Isoelastic Resurfacing Prosthesis for Distal Radius Fractures: Outcomes in 24 Cases
with at least 2 Years Follow-Up
Antoine Martins1
, Priscille Lazarus1
, Sybille Facca1,3, Stéphanie Gouzou1
, Nicolas Meyer2,3
,
Philippe Liverneaux1,3
1 Department of Hand Surgery, SOS hand, University Hospital of Strasbourg, FMTS,
University of Strasbourg, Icube CNRS 7357, 1 avenue Molière, 67000 Strasbourg, France
2 Service de Santé Publique, GMRC, University Hospital of Strasbourg, FMTS, University of
Strasbourg, 1 place de l’hôpital, 67000 Strasbourg, France
3 ICube CNRS UMR7357, Strasbourg University, 2-4 rue Boussingault, 67000 Strasbourg,
France
Corresponding Author: Liverneaux Philippe,
Hand Surgery Department, Strasbourg University Hospitals, 1 avenue Molière, F-67000
Strasbourg, France
Tel + 33 6 88 89 47 79
Philippe.liverneaux@chru-strasbourg.fr
Ne pas utiliser, pour citation, la référence française de cet article, mais celle de l’article original
paru dans Orthopaedics &Traumatology: Surgery & Research, en utilisant le DOI ci-dessus.
© 2020 published by Elsevier. This manuscript is made available under the CC BY NC user license
https://creativecommons.org/licenses/by-nc/4.0/
Version of Record: https://www.sciencedirect.com/science/article/pii/S1877051720303385
Manuscript_427384c55517871adadd3e0b0b4cd4c5
2
Résumé
Introduction : Certains auteurs ont montré l’intérêt des prothèses
unicompartimentales de resurfaçage dans le traitement des fractures articulaires
comminutives du radius distal chez les patients âgés ostéoporotiques. Cependant il existe
encore peu de travaux sur le sujet et de nouvelles études nécessitent d’être évaluer.
Hypothèse : Le but de ce travail est d’évaluer les résultats cliniques et radiologiques
après prothèse unicompartimentale de resurfaçage dans les fractures du radius distal avec
un minimum de deux ans de recul.
Matériels et méthodes : Notre série comprend 24 fractures de type C selon l’AO
opérées par prothèses Prosthelast®. L’âge moyen est de 78 ans (60 à 91). On note 22
femmes. Trois fractures sont ouvertes. Les patients ont été évalués cliniquement par une
échelle de la douleur (Echelle Visuelle Analogique), les mobilités du poignet, la force, ainsi
que par des scores fonctionnels et un bilan radiographique.
Résultats : Le recul moyen est de 55,2 mois (24 à 97). La durée moyenne du garrot est
de 61,9 minutes (37 à 126). La mobilité moyenne en flexion est de 39°, en extension de 49°,
en pronation 74°, en supination 68°. La douleur est de 2,1 (0 à 7), le quick DASH à 39,8 (9,09
à 77), le PRWE à 42,7 (5 à 95), la force à 38 (25 à 150). Une limitation douloureuse du coude
a été notée chez un patient opéré d’une prothèse totale de coude. Six CRPS et 5 reprises
chirurgicales ont été notées. On note 8 perforations de la tête radiale asymptomatique,
aucune ostéolyse périprothétique, aucune arthrose, 2 conflits entre prothèse et lunatum et
1 avec le scaphoïde. La variance ulnaire moyenne est de +0,17 mm (-1 à 7,5). Un remodelage
osseux périprothétique a été observé chez tous les patients sauf 2.
"""

# Appel de la fonction avec le texte de l'article
keywords = extract_keywords(article_text)
