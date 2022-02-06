import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("indx.html")

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    enregistrerLaPersonne(first_name,last_name,email)
    print(f"email: {email}, nom: {last_name}, prenom: {first_name}")
    return render_template("form.html")


def enregistrerLaPersonne(first_name,last_name,email):
    connection = sqlite3.connect("testData.db")
    cursor = connection.cursor()
    
    infoPersonne = (cursor.lastrowid, first_name, last_name, email)
    print(infoPersonne)
    cursor.execute("INSERT INTO testInfo VALUES(?,?,?,?)",infoPersonne)
    connection.commit()
    
    connection.close()