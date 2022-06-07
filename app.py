from flask import Flask
from model.models import db
from flask.templating import render_template
from controllers.index import index_blueprint
from controllers.programms_controller import programm_blueprint
import sqlalchemy
app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/mydataorginizer"

db.init_app(app)
app.register_blueprint(index_blueprint)
app.register_blueprint(programm_blueprint)

app.run(debug=True)