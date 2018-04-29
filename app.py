from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['username'] == "emil" and request.form['pass'] == "grillkorv":
            return redirect("/welcome/")
        else: 
            return render_template(("%s.html" % "index"), error_message = "Incorrect uname or pass")
    else:
        return render_template("%s.html" % "index")

@app.route('/welcome/', methods=['GET'])
def welcome():
    return render_template("%s.html" % "welcome")
        
