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
  submit = SubmitField('Submit')

@app.route('/',methods=("POST",'GET'))
def home():
  name = None
  form = NameForm()
  temp = None
  if form.validate_on_submit():
    name = form.name.data
    r = None
    try:
      r = requests.get(f'https://api.weatherapi.com/v1/current.json?key=49da65cf146f4636a0b181834221604&q={name}&aqi=no').json()
    except:
      r = {'current':{'temp_c' : 'An Error Occured'}}
    temp = r['current']['temp_c']
    form.name.data = ''
  return render_template('home.html',form=form, name=name,temp = temp)