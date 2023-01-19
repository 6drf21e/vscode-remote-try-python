#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import datetime
from io import BytesIO
from util import get_img

from flask import Flask
from flask import render_template, make_response
from PIL import Image

app = Flask(__name__)

# 设置模板文件的目录为 templates
app.template_folder = "templates"


@app.route("/")
def hello():
    """
    this is index page
    """
    return app.send_static_file("index.html")


# about 页面的路由
@app.route("/about2")
def about():
    """
    this is about page
    """
    # 当前日期， 输出格式为 yyyy-mm-dd HH:SS
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # 渲染模板(render_template) about.html
    return render_template("about.html", cur_time=cur_time)

# test 页面的路由
@app.route("/test")
def test():
    """
     从模板文件 testtest.html 渲染当前页面
    """
    
    return render_template("testtest.html")

# 新建一个名为 imgtest 的路由
@app.route("/imgtest")
def imgtest():
    """
    输出一张背景为黑色的图片
    """
    # 创建一个 200x200 的图片
    # img = Image.new("RGB", (200, 200), (0, 0, 0))
    img = get_img(200, 200, (0, 0, 0))
    # 创建一个 BytesIO 对象
    img_io = BytesIO()
    # 将图片保存到 BytesIO 对象中
    img.save(img_io, "PNG")
    # 将 BytesIO 对象的指针指向开头
    img_io.seek(0)
    # 生成一个响应对象
    response = make_response(img_io.read())
    # 设置响应头
    response.headers["Content-Type"] = "image/png"
    return response