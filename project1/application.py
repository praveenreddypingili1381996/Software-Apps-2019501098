import os
import datetime
from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))

#Tell Flask what SQLAlchemy database to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Link the Flask app with the database
db.init_app(app)

@app.route("/")
def index():
    return render_template("register.html") 


@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method == "POST"):
       
        email = request.form.get("email")
        
        password = request.form.get("psw")
        
       
        if not email:
            text = "Please enter username to register"
            return render_template("email.html", name=text, msg="ERROR")
        elif not password:
            text="Please provide the password"
            return render_template("email.html", name=text ,msg="ERROR")
        else:
            # text = "Success"
            dt = datetime.datetime.now()
            data = Data(username=email,password=password,timestamp=dt)
            db.session.add(data)
            db.session.commit()
            return render_template("email.html",msg="SUCCESS")
        
    return render_template("register.html")     


@app.route("/admin")
def admin():
    data1 = Data.query.all()
    return render_template("users.html", name=data1)

def main():
    app.app_context().push()
    db.create_all()    



if __name__ == "__main__":
    main()