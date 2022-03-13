import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    title = "Portfolio de Adam Deruelle"
    return render_template("index.html",title=title)

@app.route('/contact')
def contact():
    title = "Contactez-moi"
    return render_template("contact.html",title=title)

@app.route('/valide', methods=["POST"])
def valide():
    title = "Enregistré"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    enregistrerLaPersonne(first_name,last_name,email)
    print(f"email: {email}, nom: {last_name}, prenom: {first_name}")
    return render_template("valide.html",title=title)

@app.route("/my projects")
def my_projects():
    title = "Mes Projets"
    return render_template("my projects.html",title=title)

@app.route("/me")
def me():
    title = "Moi"
    return render_template("me.html",title=title)





def enregistrerLaPersonne(first_name,last_name,email):
    connection = sqlite3.connect("testData.db")
    cursor = connection.cursor()
    
    infoPersonne = (cursor.lastrowid, first_name, last_name, email)
    print(infoPersonne)
    cursor.execute("INSERT INTO testInfo VALUES(?,?,?,?)",infoPersonne)
    connection.commit()
    
    connection.close()