from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["GET"])
def check():
    age = int(request.args.get("age"))
    return render_template("checkage.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)