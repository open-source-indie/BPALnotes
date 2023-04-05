from urllib import response
from flask import Flask, url_for, send_file, jsonify, make_response
#from flask_sqlalchemy import SQLAlchemy
from os import path
from datetime import datetime
from flask_minify import minify


# database connection details

# create a database object



#create flask app and configure it / DB to models
def create_app():
        app = Flask(__name__)
        app.debug = False
            # Secret key!
        app.config['SECRET_KEY'] = '****************'
        app.config["TEMPLATES_AUTO_RELOAD"] = True
        app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        )
        

        #We can set secure cookies in response
        

            # Define DB
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            #initialize DB    
        #db = SQLAlchemy(app)
            #    from .models import User, Note
        # Models
        #class Profile(db.Model):
            # Id : Field which stores unique id for every row in
            # database table.
            # first_name: Used to store the first name if the user
            # last_name: Used to store last name of the user
            # Age: Used to store the age of the user
        #    id = db.Column(db.Integer, primary_key=True)
        #    first_name = db.Column(db.String(20), unique=False, nullable=False)
        #    last_name = db.Column(db.String(20), unique=False, nullable=False)
        #    age = db.Column(db.Integer, nullable=False)
        
            # repr method represents how one object of this datatable
            # will look like
        #    def __repr__(self):
        #        return f"Name : {self.first_name}, Age: {self.age}"
            
            
            #import views
        from .views import views
        from .auth import auth
                    #import DB

                
                #create string
            #  def __repr__(self):
            #      return '<Name %r' % self.name

            #register blueprints
        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')
        app.after_request
        def apply_caching(response):
            response.headers["X-Frame-Options"] = "SAMEORIGIN"
            response.headers["HTTP-HEADER"] = "VALUE"
            response.set_cookie('key', 'value', secure=True, httponly=True, samesite='Lax')
            return response
        return app
#def create_database(app):
    #if not path.exists('website/' + DB_NAME):
     #   db.create_all(app=app)
      #  print ( 'Database created successfully' )

    
