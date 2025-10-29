from flask import Flask, render_template, request, redirect, url_for, get_flashed_messages, flash
import os
from dotenv import load_dotenv
from api import get_reviews, save_review
from requests import HTTPError
from datetime import datetime

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")


@app.route('/')
def index():
    try:
        reviews = get_reviews()
    except HTTPError as e:
        reviews = []
        print(f"Erro ao fazer requisição de reviews: {e}")
    
    return render_template("index.html", reviews=reviews)


@app.route('/submit-review', methods=['POST'])
def submit_review():
    new_review = {
        "title": request.form.get("review-title"),
        "username": request.form.get("review-username"),
        "message": request.form.get("review-message"),
        "date": str(datetime.now().date())
    }

    try:
        review = save_review(new_review)
        flash(review, "success_post")
    except HTTPError as e:
        flash("Houve um problema ao tentar " \
             "enviar sua avaliação, tente novamente " \
             "mais tarde.", "failed_post")
        print(f"Erro ao salvar review: {e}")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
