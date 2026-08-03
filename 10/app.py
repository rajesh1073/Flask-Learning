from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    session["name"] = request.form["name"]
    session["city"] = request.form["city"]
    session["age"] = request.form["age"]

    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)