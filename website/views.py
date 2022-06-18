from flask import Blueprint,render_template,request, flash, jsonify
from flask_login import login_required, current_user
import json
views = Blueprint('views', __name__)
#first route
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")