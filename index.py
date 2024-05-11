from flask import Flask, render_template, request, make_response, redirect, url_for;
import requests as req;


import configs;
from controllers.authentication import Authentication;
from controllers.register import Register;


from configs import HOST, API_PORT




endpoint =  f'http://{HOST}:{API_PORT}/api/';
app = Flask(__name__);


# Remove Cache 
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response



#Index Route
@app.route("/", methods = ['GET', 'POST'])
def root():
    return render_template('index.html', endpoint=endpoint + "/users");







#Register Routes
@app.route("/register", methods = ['GET'])
def GETregister():
    return render_template('register.html');



@app.route("/register", methods = ['POST'])
def POSTregister():

    try:

        response = Register(request.form)
        body = response.json();


        if(response.status_code != 201):
            return render_template('register.html', error = body.get("Message"));



        return redirect(url_for("GETLogin"));


    except Exception as e:
        print(e);
        return render_template('errorPage.html', error=500), 500  




#Login Routes

@app.route("/login", methods = ['GET'])
def GETLogin():
    return render_template('login.html');




@app.route("/login", methods = ['POST'])
def POSTLogin():

    try:
        

        response = Authentication(request.form)
        body = response.json();


        if(response.status_code != 202):
            return render_template('login.html', error = body.get("Message"));


        token = body.get("x-access-token");


        resp = make_response(render_template("login.html"))
        resp.set_cookie('token', token)

        return resp;

    except Exception as e:
        return render_template('errorPage.html', error=500), 500  








































@app.route("/main", methods = ['GET', 'POST'])
def index():
    



    return render_template('main.html');


       


#Server running on:
app.run(host=configs.HOST, port=configs.PORT, debug=True);