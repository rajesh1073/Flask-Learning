from flask import Flask

app=Flask(__name__)

# @app.route("/")
def info():
    return "hello world from info function"

app.add_url_rule("/home","info",info)


if __name__=="__main__":
    app.run()