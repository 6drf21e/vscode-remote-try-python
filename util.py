from PIL import Image
import io
import datetime
import random


# 传入值为 0-1 的浮点数 v ，和概率 deep， 根据 v * deep / 1 的概率返回 True
def get_random_bool(v, deep=1):
    """
    传入值为 0-1 的浮点数 v ，和概率 deep， 根据 v * deep / 1 的概率随机返回 True
    """
    # print(v)
    if random.random()  >= v * deep:
        return True
    else:
        return False


# 返回一张图片 宽度为 w 高度 为 h， 背景色为 bg_color ，生成从上到下递减的随机像素点
def get_img(w, h, bg_color):
    """
    返回一张图片 宽度为 w 高度 为 h 背景色为 bg_color
    生成从上到下递减的随机像白色像素点
    返回 image 对象
    """
    # 创建一个 w x h 的图片
    img = Image.new("RGB", (w, h), bg_color)
    # 获取图片的像素点
    pixels = img.load()
    # 生成从上到下递减的随机像素点
    for i in range(w):
        for j in range(h):
            if get_random_bool(j / h):
                # print(get_random_bool(j / h))
                # 生成随机像素点
                pixels[i, j] = (255, 255, 255)
    return img
