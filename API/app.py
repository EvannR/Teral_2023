from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titre = "Titre depuis Python"
    contenu = "Contenu depuis Python"
    return render_template('index.html', titre=titre, contenu=contenu)


#if __name__ == "app":
#    app.run()