import cv2
import os
import matplotlib.pyplot as plt
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
    return redirect("img/0.jpg/0")

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
		im.thumbnail((500,500))
		im.save('C:/Users/luoyujia/flasky/static/test1.jpg')
		detect('test0.jpg')
		im=Image.open('C:/Users/luoyujia/flasky/static/face.jpg')
		im.thumbnail((500,500))
		im.save('C:/Users/luoyujia/flasky/static/face1.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='face1.jpg',num=num,val1=time.time())
	if num=='1':
		version = random.randint(0,1000);
		im=Image.open('C:/Users/luoyujia/flasky/static/'+filename)
		im=im.convert('RGB')
		im.save('C:/Users/luoyujia/flasky/static/test0.jpg')
		im.thumbnail((500,500))
		im.save('C:/Users/luoyujia/flasky/static/test1.jpg')
		detecteyes('test0.jpg')
		im=Image.open('C:/Users/luoyujia/flasky/static/face.jpg')
		im.thumbnail((500,500))
		im.save('C:/Users/luoyujia/flasky/static/face1.jpg')
		return render_template("imageprocessing.html",filename1='test1.jpg',filename2='face1.jpg',num=num,val1=time.time())

def detect(filename):
    # haarcascade_frontalface_default.xml存储在package安装的位置
    #face_cascade = cv2.CascadeClassifier("D:\FaceRuyi\data\haarcascade_eye.xml")
    face_cascade = cv2.CascadeClassifier("C:/Users/luoyujia/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    os.chdir('C:/Users/luoyujia/flasky/static/')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #传递参数是scaleFactor和minNeighbors,分别表示人脸检测过程中每次迭代时图像的压缩率以及每个人脸矩形保留近邻数目的最小值
    #检测结果返回人脸矩形数组
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow("Face Detected!")
    cv2.imshow("Face Detected!", img)
    cv2.imwrite("Face.jpg", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
def detecteyes(filename):
    # haarcascade_frontalface_default.xml存储在package安装的位置
    #face_cascade = cv2.CascadeClassifier("D:\FaceRuyi\data\haarcascade_eye.xml")
    face_cascade = cv2.CascadeClassifier("C:/Users/luoyujia/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye.xml")
    os.chdir('C:/Users/luoyujia/flasky/static/')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #传递参数是scaleFactor和minNeighbors,分别表示人脸检测过程中每次迭代时图像的压缩率以及每个人脸矩形保留近邻数目的最小值
    #检测结果返回人脸矩形数组
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow("Face Detected!")
    cv2.imshow("Face Detected!", img)
    cv2.imwrite("face.jpg", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
