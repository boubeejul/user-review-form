from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def index():
    #TODO: get reviews from api

    reviews = [{
        "username" : "Usuário",
        "title" : "Achei legal, mas...",
        "message" : "Ainda nao testei",
        "date": "24/10/2025"
    }]
    return render_template("index.html", reviews=reviews)

@app.route('/submit-review', methods=['POST'])
def submit_review():
    title = request.form.get("review-title")
    username = request.form.get("review-username")
    message = request.form.get("review-message")
    
    #TODO: post review to api

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
