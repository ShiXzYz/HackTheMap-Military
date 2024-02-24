from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "does this do anything"
    
    from .views import views
    from .results import results

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(results, url_prefix='/')

    return app