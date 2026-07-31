from flask import Flask
app=Flask(__name__)

@app.route("/add/<int:num1>/<int:num2>")
def addition(num1,num2):
    return "Addition is:"+str(num1+num2)

@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1,num2):
    return "Multiply is:"+str(num1*num2)


if __name__=="__main__":
    app.run()
    
