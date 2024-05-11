from flask import Flask, render_template, request, make_response, jsonify, redirect;
import requests as req;


import configs;
from controllers.authentication import Authentication

from configs import HOST, API_PORT




endpoint =  f'http://{HOST}:{API_PORT}/api/';
app = Flask(__name__);






#Index Route
@app.route("/", methods = ['GET', 'POST'])
def root():
    return render_template('index.html', endpoint=endpoint + "/users");





#Login Routes

@app.route("/login", methods = ['GET'])
def GETLogin():
    return render_template('login.html');



@app.route("/login", methods = ['POST'])
def POSTLogin():


    response = Authentication(request.form)
    body = response.json();


    if(response.status_code != 202):
        return render_template('login.html', error = body.get("Message"));



    token = body.get("x-access-token");


    resp = make_response(render_template("login.html"))
    resp.set_cookie('token', token)

    return resp;







































@app.route("/register", methods = ['GET', 'POST'])
def register():
    



    return render_template('register.html');


@app.route("/index", methods = ['GET', 'POST'])
def index():
    



    return render_template('index.html');


       


#Server running on:
app.run(host=configs.HOST, port=configs.PORT, debug=True);