from flask_bootstrap import Bootstrap
from flask import Flask,render_template,session,redirect,url_for,flash
from flask_moment import Moment
from datetime import datetime

app=Flask(__name__)
moment=Moment(app)
app.config['SECRET_KEY']='hard to guess string'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

bootstrap=Bootstrap(app)
"""
@app.route('/')
def index():
	return render_template('index.html')
	"""
@app.route('/user/<id>')
def get_user(id):
	return render_template('user.html',name=id)
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500
@app.route('/name/<table>')
def select(table):
	return render_template('user.html',name=id)
"""
from flask import abort 
"""

class NameForm(FlaskForm):
	name=StringField('What is your name?',validators=[DataRequired()])
	submit=SubmitField('Submit')
	
@app.route('/',methods=['GET','POST'])
def index():
	name=None
	form=NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('看起来你更改了你的名字')
		session['name']=form.name.data
		return redirect(url_for('index'))
		#form.name.data=''
	return render_template('index.html',form=form,name=session.get('name'))
