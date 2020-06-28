
from flask import Flask,render_template,session,redirect,url_for,flash
from flask_moment import Moment
from datetime import datetime
import pymysql
app=Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
moment=Moment(app)
app.config['SECRET_KEY']='hard to guess string'


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

"""
@app.route("/")
def index():
    return render_template("index.html")
#,current_time=datetime.utcnow()
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

@app.route("/name/<table>")
def select(table):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'cuc')
    cursor = db.cursor()

    sql = "select * from %s"%table
    try:
        count=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()

    except:
        print("Error")
    db.close()

    return render_template("select.html",rs=rs,count=count)

	

@app.route("/name/<table>/<num>")
def get_detail(table,num):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'cuc')
    cursor = db.cursor()

    sql = "select * from %s limit %s,1"% (table,num)
    try:
        count=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()
    return render_template("news.html",rs=rs)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001)
