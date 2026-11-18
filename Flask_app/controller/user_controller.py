#Just for learning
from app import app
from model.user_model import user_model
object = user_model()
@app.route("/welcome/usersignup")
def usercontrollersignup():
    return object.user_signup_model()