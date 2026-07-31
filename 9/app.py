from flask import *
app=Flask(__name__)
 
 
@app.route("/")
def home():
    return render_template("cookiepage.html")
 
@app.route("/cookie")
def addcookie():
    resp = make_response(render_template("readcookie.html"))
    resp.set_cookie('username', request.args.get("username"))
    resp.set_cookie('usercity', request.args.get("city"))
    return resp

@app.route("/showcookie")
def showcook():
    name=request.cookies.get('username')
    city=request.cookies.get('usercity')
    return "Data from cookies is name "+name+ "city is "+city

 
 
if __name__=='__main__':
    app.run()