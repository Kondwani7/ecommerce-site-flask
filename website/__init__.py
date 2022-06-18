from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dhdododpw'
    #import our  views routing and authetication
    from .views import views
    from .auth import auth
    #register the views and auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    return app