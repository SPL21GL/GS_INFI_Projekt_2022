from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy

index_blueprint = Blueprint('index_blueprint', __name__)
