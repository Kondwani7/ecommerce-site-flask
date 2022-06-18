from flask import Blueprint

views = Blueprint('views', __name__)
#first route
@views.route('/')
def home():
    return "<h1>Website</h1>"