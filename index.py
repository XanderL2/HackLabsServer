from flask import Flask, render_template, request;
app = Flask(__name__);


#CODIGO:

@app.route("/", methods = ['GET', 'POST'])
def form_user():
    

    return render_template('index.html');


        


#Server running on:
app.run(host="localhost", port=5000, debug=True);
