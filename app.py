import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/valide', methods=["POST"])
def valide():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    enregistrerLaPersonne(first_name,last_name,email)
    print(f"email: {email}, nom: {last_name}, prenom: {first_name}")
    return render_template("form.html")

@app.route("/my projects")
def my_projects():
    return render_template("my projects.html")

@app.route("/me")
def me():
    return render_template("me.html")





def enregistrerLaPersonne(first_name,last_name,email):
    connection = sqlite3.connect("testData.db")
    cursor = connection.cursor()
    
    infoPersonne = (cursor.lastrowid, first_name, last_name, email)
    print(infoPersonne)
    cursor.execute("INSERT INTO testInfo VALUES(?,?,?,?)",infoPersonne)
    connection.commit()
    
    connection.close()