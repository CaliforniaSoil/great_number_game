from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'aKey'



@app.route('/', methods = ['GET'])
def index():
    if "guess" not in session:
	    session["guess"] = 0 
    a1 = ""
    session['num'] = ""

    if not session['num']:
        session['num'] = random.randint(1,101)
    
    return render_template("index.html", num = session['num'], guess = session['guess'])

@app.route('/process', methods =["GET", 'POST'])
def result():
    session['guess'] = request.form['guess']
    a1 = int(session['guess'])
    a2 = session['num']

        
    return render_template("index.html", num = session['num'], guess = session['guess'], a1 = a1, a2 = a2)

    

app.run(debug=True)
