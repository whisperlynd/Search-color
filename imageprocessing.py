
from flask import Flask,render_template,session,redirect,url_for,flash,request,send_from_directory, make_response, jsonify, abort
from flask_moment import Moment
from datetime import datetime
import pymysql
import random
app=Flask(__name__)
import time
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
moment=Moment(app)
app.config['SECRET_KEY']='hard to guess string'


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from PIL import Image, ImageFilter
from numpy import *
from werkzeug.utils import secure_filename
@app.route("/")
def index():
	return redirect("img/1.jpg/0")

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    os.chdir('C:/Users/luoyujia/flasky/static/')
    directory = os.getcwd()
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response

@app.route("/img/<filename>/<num>", methods=['POST', 'GET'])
def picture(filename,num):
	version = random.random()*100000;
	if request.method == 'POST':
		f = request.files['file']
		basepath = os.path.dirname(__file__)
		upload_path = os.path.join(basepath, "static", secure_filename(f.filename+""+str(version)))
		f.save(upload_path)
		return redirect(url_for('picture',filename=secure_filename(f.filename+""+str(version)),num=0))
	if num=='0':
		version = random.randint(0,1000);
		im=Image.open('C:/Users/luoyujia/flasky/static/'+filename)
		im=im.convert('RGB')
		im.save('C:/Users/luoyujia/flasky/static/test0.jpg')
		im.thumbnail((300,300))
		im.save('C:/Users/luoyujia/flasky/static/test1.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='test1.jpg',num=num,val1=time.time())
	if num=='1':
		os.chdir('C:/Users/luoyujia/flasky/static/')
		im=Image.open('test0.jpg').convert("L")
		im.save('C:/Users/luoyujia/flasky/static/test2.jpg')
		im.thumbnail((300,300))
		im.save('C:/Users/luoyujia/flasky/static/test3.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='test3.jpg',num=num)
	if num=='2':
		os.chdir('C:/Users/luoyujia/flasky/static/')
		im=Image.open('test0.jpg').transpose(Image.FLIP_LEFT_RIGHT)
		im.save('C:/Users/luoyujia/flasky/static/test2.jpg')
		im.thumbnail((300,300))
		im.save('C:/Users/luoyujia/flasky/static/test3.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='test3.jpg',num=num)
	if num=='3':
		os.chdir('C:/Users/luoyujia/flasky/static/')
		im=Image.open('test0.jpg').transpose(Image.FLIP_TOP_BOTTOM)
		im.save('C:/Users/luoyujia/flasky/static/test2.jpg')
		im.thumbnail((300,300))
		im.save('C:/Users/luoyujia/flasky/static/test3.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='test3.jpg',num=num)
	if num=='4':
		os.chdir('C:/Users/luoyujia/flasky/static/')
		im=Image.open('test0.jpg').filter(ImageFilter.GaussianBlur)
		im.save('C:/Users/luoyujia/flasky/static/test2.jpg')
		im.thumbnail((300,300))
		im.save('C:/Users/luoyujia/flasky/static/test3.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='test3.jpg',num=num)
		