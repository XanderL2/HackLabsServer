from flask import Flask, render_template, request, make_response, redirect, url_for, session;


#Controllers
import configs;
from controllers.authentication import Authentication;
from controllers.register import Register;
from controllers.sessionController import EstablishSesion;
from controllers.main import GetUserInfo, GetUserStatistics, GetUsers;
from controllers.settings import PatchData, SavePhoto;




#Analysis
from analysis.FavoriteTools import FavoriteTools
from analysis.TopUsers import TopUsers;
from analysis.activityLog import LogsPerUser;







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

    
    users  = GetUsers();
    userId = session.get("userId");

    userInfo = GetUserInfo(userId, users);
    userStatistics = GetUserStatistics(userId);    


    tools = FavoriteTools(userId);
    topUsers = TopUsers(users);
    graphicUser = LogsPerUser(userId);




    return render_template('main.html', 
                           graphicUser = graphicUser,
                           user = userInfo, 
                           userStatistics = userStatistics, 
                           users = users,
                           tools = tools,
                           topUsers = topUsers
                        
                           
                    );      


       

@app.route('/main/<int:userId>')
def userProfile(userId):


    users  = GetUsers()


    if(type(userId) != int):
        return render_template('errorPage.html', error=400, e="Incorrect id!"), 400  



    ExistsUser = GetUserInfo(userId, users);
    if(ExistsUser == False):
        return render_template('errorPage.html', error=404, e="User Not Exists!"), 404  



    
    userStatistics = GetUserStatistics(userId);    
    tools = FavoriteTools(userId);
    topUsers = TopUsers(users);
    graphicUser = LogsPerUser(userId);




    return render_template('profiles.html', 
                           graphicUser = graphicUser,
                           sessionPhoto = GetUserInfo(session["userId"], users).get("photo"),
                           user = ExistsUser, 
                           userStatistics = userStatistics, 
                           users = users,
                           tools = tools,
                           topUsers = topUsers

                    );      











@app.route("/settings", methods = ['GET'])
def GETsettings():
    

    token = session.get("token")    
    return render_template('settings.html', token = token)

    

@app.route("/settings", methods = ['POST'])
def POSTsettings():
    
    
    response = PatchData(request, session)
   
    

    if(response == False): 
        return render_template('settings.html', error = "Incorrect form!");


    if(response.status_code >= 400): 

        error = response.json(); 
        error = error.get("Message")
        
        return render_template('settings.html', error = error);


    SavePhoto(request.files, session)

    return render_template('settings.html', error=False);





    


    
    

    































#Server running on:
app.run(host=configs.HOST, port=configs.PORT, debug=True);