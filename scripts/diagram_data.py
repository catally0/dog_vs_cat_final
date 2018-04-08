import os
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image

# 读取数据集各个图片的大小，并保存到文件中
def load_data_size(data_path, name):
    # 读取宽高
    all_data = []
    for i in range(1,12499):
        pic = "%s/train/%s.%s.jpg" % (data_path, name, i)
        im = Image.open(pic)
        w, h = im.size
        line = dict()
        line["a_pic"] = i
        line["width"] = w
        line["high"] = h
        all_data.append(line)

    # 写入
    df = pd.DataFrame(all_data)
    df.to_excel("data_%s.xlsx"%name, index=False)

# 绘制散点图
def draw(file):
    pass

# main
def main():
    # 读取图片信息，并记录到文件，供后续处理
    load_data_size("../../temp/competitions/dogs-vs-cats-redux-kernels-edition", "dog")
    load_data_size("../../temp/competitions/dogs-vs-cats-redux-kernels-edition", "cat")

# 运行
if __name__ == '__main__':
    main()
