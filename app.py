from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "hello"

#Form Class 
class NameForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  submit = SubmitField('Submit')

@app.route('/',methods=("POST",'GET'))
def home():
  name = None
  form = NameForm()
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
  return render_template('home.html',form=form, name=name)