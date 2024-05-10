from flask import Flask, render_template, request;
import requests as req;


import configs;
import controllers.authentication as auth;








app = Flask(__name__);



@app.route("/", methods = ['GET', 'POST'])
def root():
    

    response = auth.AuthUser("password", "xd");



    return render_template('index.html');



@app.route("/login", methods = ['GET', 'POST'])
def register():
    



    return render_template('login.html');




@app.route("/register", methods = ['GET', 'POST'])
def login():
    



    return render_template('register.html');


@app.route("/index", methods = ['GET', 'POST'])
def index():
    



    return render_template('index.html');


       


#Server running on:
app.run(host=configs.HOST, port=configs.PORT, debug=False);