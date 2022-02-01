import os
from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config.from_mapping(
        FROM_EMAIL=os.environ.get('FROM_EMAIL'),
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )
    
    from . import db
    
    db.init_app(app)
    from . import mail
    app.register_blueprint(mail.bp)
    return app
