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
    print(f"email: {email}, nom: {last_name}, prenom: {first_name}")
    return render_template("form.html")