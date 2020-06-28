#! /usr/bin/env python

from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
from flask import  Flask, request, render_template, Response,send_from_directory,url_for,redirect
import os
def getColors(file):
    image = Image.open(file).convert("RGB")
    image.thumbnail((100,100))
    image_array = np.array(image)
    shape = image_array.shape[:-1]
    print(shape)
    image_array = image_array.reshape((shape[0] * shape[1], 3))

    clf = KMeans(n_clusters=6, random_state=9)
    clf.fit(image_array)
    centers = clf.cluster_centers_
    return np.array(centers, dtype=np.uint8)


app=Flask(__name__)
@app.route('/')
def first_flask():
    return render_template("index2.html")

@app.route('/up_file', methods=['GET', 'POST'])
def up_file():
    if request.method == "POST":
        file = request.files['file']
        print("start!")
        colors = getColors(file)
        str = ""
        print("end!")
        for i in colors:
            str +="rgb({0},{1},{2}):".format(i[0],i[1],i[2])
        return str

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000", debug=True)
