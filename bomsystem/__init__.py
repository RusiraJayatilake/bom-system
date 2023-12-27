from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bom.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

def run_app():

    #Blueprint regisrations
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()
        print('Database created successfully')

    return app
