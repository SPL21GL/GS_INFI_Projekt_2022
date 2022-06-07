from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from model.models import db,Programme

programm_blueprint = Blueprint('programm_blueprint', __name__)

@programm_blueprint.route("/programms")
def index():

    return render_template("programms.html")