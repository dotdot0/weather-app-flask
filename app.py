from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "hello"

#Form Class 
class NameForm(FlaskForm):
  name = StringField('Name of the city', validators=[DataRequired()])
  submit = SubmitField('Search 🔍')

@app.route('/',methods=("POST",'GET'))
def home():
  name = None
  form = NameForm()
  temp = None
  if form.validate_on_submit():
    name = form.name.data
    r = requests.get(f'https://api.weatherapi.com/v1/current.json?key=49da65cf146f4636a0b181834221604&q={name}&aqi=no').json()
    if not 'error' in r:
      temp = r['current']['temp_c']
      form.name.data = ''

    else:
      temp = r['error']['message']
      form.name.data = ''
      
  return render_template('home.html',form=form, name=name,temp = temp)