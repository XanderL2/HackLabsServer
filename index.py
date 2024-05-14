from flask import Flask, render_template, request, make_response, redirect, url_for, session;


#Modules
import configs;
from controllers.authentication import Authentication;
from controllers.register import Register;
from controllers.sessionController import EstablishSesion;
from controllers.main import GetUserInfo, GetUserStatistics, GetUsers;
from analysis.FavoriteTools import FavoriteTools
from analysis.TopUsers import TopUsers;







#Environment Variables
from configs import HOST, API_PORT, SECRET, API_PROTOCOL




endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';
app = Flask(__name__);
app.secret_key = SECRET;



#Index Route
@app.route("/", methods = ['GET', 'POST'])
def root():
    return render_template('index.html', endpoint=endpoint + "/users");




#Register Routes
@app.route("/register", methods = ['GET'])
def GETregister():
    if (session.get("userId") != None): return redirect(url_for("index"));
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
        return render_template('errorPage.html', error=500, e=e), 500  





#Login Routes
@app.route("/login", methods = ['GET'])
def GETLogin():
    if (session.get("userId") != None): return redirect(url_for("index"));
    return render_template('login.html');



@app.route("/login", methods = ['POST'])
def POSTLogin():


    try:
        
        response = Authentication(request.form)
        body = response.json();


        if(response.status_code != 202):
            return render_template('login.html', error = body.get("Message"));


        token = body.get("x-access-token");


        EstablishSesion(token);



        resp = make_response(redirect(url_for("index")))
        resp.set_cookie('token', token)


        return resp;

    except Exception as e:

        return render_template('errorPage.html', error=500, e=e), 500  





#! Authentication middleware
@app.before_request
def VerifyAuthentication():


    isNotPublicRoute = request.endpoint not in ['root', 'GETregister', 'POSTregister', 'GETLogin', 'POSTLogin'];
    isNotStaticRoute = not request.path.startswith('/static')
    isUserNotAuthenticated = 'userId' not in session

    
    if isNotPublicRoute and isNotStaticRoute and isUserNotAuthenticated:
        return redirect(url_for('GETLogin')); 

    


#! Privates Routes
@app.route("/main", methods = ['GET'])
def index():


    userId = session.get("userId");

    userInfo = GetUserInfo(userId)[0];
    userStatistics = GetUserStatistics(userId);    
    users = GetUsers();
    tools = FavoriteTools(userId);
    topUsers = TopUsers();







    return render_template('main.html', 
                           username=userInfo.get("username"), 
                           userStatistics=userStatistics, 
                           users = users,
                           tools = tools,
                           topUsers = topUsers
                    );      


       
























@app.route("/statistics", methods = ['GET'])
def statistics():

    

    xd = TopUsers();


    print(xd)



    return "xd"










#Server running on:
app.run(host=configs.HOST, port=configs.PORT, debug=False);