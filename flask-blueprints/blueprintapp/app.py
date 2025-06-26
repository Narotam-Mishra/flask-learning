from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create SQLAlchemy instance without binding to specific app (allows multiple apps)
db = SQLAlchemy()

def create_app():
    # create Flask app instance with custom template directory
    app = Flask(__name__, template_folder='templates')
    
    # set database connection string to SQLite file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'

     # initialize SQLAlchemy with the Flask app (late binding)
    db.init_app(app)

    # import and register all blueprints
    from blueprintapp.core.routes import core
    from blueprintapp.todos.routes import todos
    from blueprintapp.people.routes import people
    
    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(todos, url_prefix='/todos')
    app.register_blueprint(people, url_prefix='/people')

    # initialize Flask-Migrate for database migrations
    migrate = Migrate(app, db)

    # return configured Flask application instance
    return app