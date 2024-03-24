import os
from flask import Flask
from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    
    #Config 
    app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")
    
    # Connect libraries
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)
    
    from controllers.workout_controller import workout_bp
    app.register_blueprint(workout_bp)
    
    return app