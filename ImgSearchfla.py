from flask import Flask, render_template, request, redirect, url_for
import os
import re
import requests
from flask_moment import Moment
import time
from flask_bootstrap import Bootstrap
from datetime import datetime
import random
from collections import namedtuple    #命名元组
from math import sqrt                 #开方函数
import matplotlib.pyplot as plt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import json
from PIL import Image, ImageFilter
from werkzeug.utils import secure_filename
import jieba# 导入 jieba

app = Flask(__name__)


# 清空图片文件夹
def deletefile(filepath):
    for i in os.listdir(filepath):
        path_file = os.path.join(filepath, i)
        if os.path.isfile(path_file):
            os.remove(path_file)


def ImgDownload(keyword,start):
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&ct=201326592&v=flip'
    result = requests.get(url)
    html = result.text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 0
    maxsize = 204800  # 200kb以下
    minsize = 1024    # 1kb以上
    for each in pic_url:
        if i > 9:
            break
        try:
            pic = requests.get(each, timeout=5)
            '''
            这部分有点问题
            if int(pic.headers['Content-Length']) > maxsize or int(pic.headers['Content-Length']) < minsize:
                continue
            '''
        except requests.exceptions.ConnectionError:
            print('error')
            continue
        dir = 'C:/Users/luoyujia/flasky/static/images/'+ str(start+i) + '.jpg'
        print(start+i)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
    return i


@app.route("/")
def index():
    deletefile('C:/Users/luoyujia/flasky/static/images/')
    os.chdir('C:/Users/luoyujia/flasky/static/')
    return render_template("index.html")
@app.route("/detail/<num>")
def detail(num):
	num="images/"+num+".jpg"
	list1=list(colorz("C:/Users/luoyujia/flasky/static/"+num, n=1))
	print("!@!!#@!")
	print(list1)
	return render_template("hi.html",num=num,list=list)

@app.route("/search",methods=["GET", "POST"])
def search():
	start=0
	color_data=[]
	keyword = request.args.get('keyword', type=str)
	if keyword:
		seg_list = jieba.lcut(keyword, cut_all=False)
		for keyword in seg_list:
			print(keyword)
			n=ImgDownload(keyword,start)#网络爬虫函数
			print('!')
			print(n)
			print(keyword)
			print(start)
			count=0
			for num in range(start,start+n):
				try:
					im=Image.open('C:/Users/luoyujia/flasky/static/images/'+ str(num) + '.jpg')
					im=im.convert('RGB')
					im.thumbnail((50,50))
					im.save('C:/Users/luoyujia/flasky/static/test1.jpg')
					list1=list(colorz("C:/Users/luoyujia/flasky/static/test1.jpg", n=1))
					color_data.append(list1)
					count+=1
				except OSError:
					continue
				print(num)
			start+=count
		print(color_data)
		print(start)
		return render_template("colorpic.html",data=color_data,size=start)
	return render_template('index.html')
       


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
	

Point = namedtuple('Point', ('coords', 'n', 'ct'))   #命名元组，Point为元组名，后面是字段名
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))   #命名元组，Cluster为元组名，后面是字段名
rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))    #定义了一个lambda表达式，rgb为他的名字

def get_points(img):
    points = []   #list,其元素为命名元组Point
    w, h = img.size    #原始图像尺寸
    #print(w,h)
    for count, color in img.getcolors(w * h):     #获得图像的色彩和这种色彩的像素个数
        points.append(Point(color, 3, count))
    #print(points[0])                              #打印一下第一个元素
    return points

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
