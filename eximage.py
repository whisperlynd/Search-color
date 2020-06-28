# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import cv2
import time
import numpy as np
from datetime import timedelta

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)
# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)


@app.route('/')
def index():
    return redirect("/upload")

# @app.route('/upload', methods=['POST', 'GET'])
@app.route('/upload', methods=['POST', 'GET'])  # 添加路由
def upload():
    if request.method == 'POST':
        f = request.files['file']

        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})

        user_input = request.form.get("name")

        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # upload_path = os.path.join(basepath, 'static/images','test.jpg')  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)

        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)
        cv2.imwrite(os.path.join(basepath, 'static/images', 'test.jpg'), img)



        if user_input == "灰度":
            img1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            cv2.imwrite(os.path.join(basepath, 'static/images', 'test1.jpg'), img1)
        elif user_input == "负片":
            # divide a multi-channel array into three single-channel arrays
            b, g, r = cv2.split(img)
            b = 255 - b
            g = 255 - g
            r = 255 - r
            # change the arrays's value by indexing
            img[:, :, 0] = b
            img[:, :, 1] = g
            img[:, :, 2] = r
            cv2.imwrite(os.path.join(basepath, 'static/images', 'test1.jpg'), img)
        elif user_input == "锐化":
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
            dst = cv2.filter2D(img, -1, kernel=kernel)
            cv2.imwrite(os.path.join(basepath, 'static/images', 'test1.jpg'), dst)
        elif user_input == "高斯模糊":
            img_ = cv2.GaussianBlur(img, ksize=(21, 21), sigmaX=0, sigmaY=0)
            cv2.imwrite(os.path.join(basepath, 'static/images', 'test1.jpg'), img_)

        return render_template('upload_ok.html', userinput=user_input, val1=time.time())

    return render_template('upload.html')


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = "/Users/yooc/PycharmProjects/py1/static/images"  # 假设在当前目录
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)

