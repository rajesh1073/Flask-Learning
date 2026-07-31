from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Hardcoded credentials
    if username == "admin" and password == "1234":
        return render_template("main.html", user=username)
    else:
        return "Invalid Username or Password"

if __name__ == "__main__":
    app.run(debug=True)