
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


@app.route("/")
def index():
    #return render_template("index.html")
    return redirect("name/book250")



@app.route("/name/<table>")
def select(table):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'doubandushu')
    cursor = db.cursor()
    sql = "select  * from %s"%table
    try:
        rscount=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()

    return render_template("selectdouban.html",rs=rs)
	
@app.route("/name/<table>/<num>")
def select_page(table,num):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'doubandushu')
    cursor = db.cursor()
    sql = "select * from %s limit %s,25"% (table,num)
    try:
        rscount=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()

    return render_template("selectdouban.html",rs=rs)
	

"""
@app.route("/name/<table>/<bookID>")
def get_detail(table,bookID):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'doubandushu')
    cursor = db.cursor()
    id=str(int(int(bookID)+750))
    sql = "select * from %s limit %s,1"% (table,id)
    try:
        count=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()
    return render_template("newsdouban.html",rs=rs)

@app.route("/name/<table>/<num>")
def get_detail(table,num):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'cuc')
    cursor = db.cursor()

    sql = "select * from %s where Id=%s"% (table,num)
    try:
        count=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()
    return render_template("newsdouban.html",rs=rs)
"""	

@app.route("/name/<table>/detail/<num>")
def get_detail(table,num):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'doubandushu')
    cursor = db.cursor()

    sql = "select * from %s where Id = %s"% (table,num)
    try:
        count=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()
    return render_template("newsdouban.html",rs=rs)
	
if __name__=="__main__":
    app.run(host='0.0.0.0',port="5001")