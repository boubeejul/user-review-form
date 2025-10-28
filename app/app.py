from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    #TODO: get reviews from api
    return render_template("index.html")

@app.route('/submit-review', methods=['POST'])
def submit_review():
    title = request.form.get("review-title")
    username = request.form.get("review-username")
    message = request.form.get("review-message")
    
    #TODO: post review to api
    return redirect("/")
    

if __name__ == '__main__':
    app.run(debug=True)
