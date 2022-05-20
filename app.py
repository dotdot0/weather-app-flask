from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/')
def home():
  return {"message":"Hello World!"}