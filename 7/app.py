from flask import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/validate",methods=["GET"])
def validate():
    username=request.args.get("uname")
    password=request.args.get("pwd")
    if username=="Rajesh" and password=="77468":
        fruits = ["Apple", "Banana", "Mango", "Orange"]
        return render_template("main.html",fruits=fruits)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
