from flask_bootstrap import Bootstrap
from flask import Flask,render_template
app=Flask(__name__)
bootstrap=Bootstrap(app)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/user/<id>')
def get_user(id):
	return render_template('user.html',name=id)
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500
	
"""
from flask import abort 
"""

