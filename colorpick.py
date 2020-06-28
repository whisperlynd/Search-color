
from flask import Flask,render_template,session,redirect,url_for,flash,request,send_from_directory, make_response, jsonify, abort
from flask_moment import Moment
from datetime import datetime
import random
app=Flask(__name__)
import time
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
moment=Moment(app)
app.config['SECRET_KEY']='hard to guess string'
from collections import namedtuple    #命名元组
from math import sqrt                 #开方函数
import matplotlib.pyplot as plt
import os                             #操作系统API
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import json
from PIL import Image, ImageFilter
from werkzeug.utils import secure_filename

Point = namedtuple('Point', ('coords', 'n', 'ct'))   #命名元组，Point为元组名，后面是字段名
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))   #命名元组，Cluster为元组名，后面是字段名

def get_points(img):
    points = []   #list,其元素为命名元组Point
    w, h = img.size    #原始图像尺寸
    #print(w,h)
    for count, color in img.getcolors(w * h):     #获得图像的色彩和这种色彩的像素个数
        points.append(Point(color, 3, count))
    #print(points[0])                              #打印一下第一个元素
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))    #定义了一个lambda表达式，rgb为他的名字

def colorz(filename, n):
    img = Image.open(filename)
    #plt.imshow(img)
    #plt.show()
    img.thumbnail((200, 200))
    w, h = img.size
    #print(w,h)

    points = get_points(img)
    clusters = kmeans(points, n, 1)
   
    rgbs = [map(int, c.center.coords) for c in clusters]

    return map(rtoh, rgbs)

def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))

def oushi(p1,p2):
    myoushi=0
    for i in range(p1.n):
        myoushi=myoushi+(p1.coords[i]-p2.coords[i])**2
    myoushi=sqrt(myoushi)
    return myoushi
        
def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]
    for c in clusters:
        print(c)
    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters

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
	if request.method == 'POST':
		f = request.files['file']
		basepath = os.path.dirname(__file__)
		upload_path = os.path.join(basepath, "static", secure_filename(f.filename))
		f.save(upload_path)
		return redirect(url_for('picture',filename=secure_filename(f.filename),num=0))
	if num=='0':
		im=Image.open('C:/Users/luoyujia/flasky/static/'+filename)
		im=im.convert('RGB')
		im.save('C:/Users/luoyujia/flasky/static/test0.jpg')
		im.thumbnail((300,300))
		im.save('C:/Users/luoyujia/flasky/static/test1.jpg')
		list1=list(colorz("C:/Users/luoyujia/flasky/static/test1.jpg", n=8))
		return render_template("colorpick.html",filename1='test1.jpg',filename2='test1.jpg',num=num,list1=list1)