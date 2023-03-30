# -*- coding: utf-8 -*-
'''
 CIFAR-10 是一个用来学习的非常好的图片数据集, http://www.cs.toronto.edu/~kriz/cifar.html
 手动下载,解压，
    examples/ImgClassify/Cifar_Classify/data/cifar-10-batches-py/batches.meta
                                                                /data_batch_1
                                                                /data_batch_2

 CIFAR-10图片有这么10 种类型
    airplane
    automobile
    bird
    cat
    deer
    dog
    frog
    horse
    ship
    truck
'''

import glob
import os.path

import cv2
import numpy as np

from examples.ImgClassify.Cifar_Classify.DataLoader import data_loader_test

labels = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
def save_train_data():
    paths = glob.glob("data/cifar-10-batches-py/data_batch_*")
    save_path = "data/train_data"
    for item in paths:
        dict = unpickle(item)
        for im_index, im_data in enumerate(dict[b'data']):
            label_index = dict[b'labels'][im_index]
            file_name = dict[b'filenames'][im_index]
            # print(dict[b'labels'][im_index], end="\t")
            # print(dict[b'filenames'][im_index])

            label_name = labels[label_index ]
            im_data = np.reshape(im_data, [3, 32, 32])
            im_data = np.transpose(im_data, [1, 2, 0])

           # cv2.imshow("im_data", cv2.resize(im_data, (200, 200)))
           # cv2.waitKey(0)
            if not os.path.exists("{}/{}".format(save_path, label_name)):
                os.mkdir("{}/{}".format(save_path, label_name))
            cv2.imwrite("{}/{}/{}".format(save_path, label_name, file_name.decode('utf-8')), im_data)


def save_test_data():
    paths = glob.glob("data/cifar-10-batches-py/test_batch*")
    test_path = "data/test_data"
    for item in paths:
        dict = unpickle(item)
        print(dict.keys())
        for im_index, im_data in enumerate(dict[b'data']):

            label_index = dict[b'labels'][im_index]
            file_name = dict[b'filenames'][im_index]
            label_name = labels[label_index ]
            print("writing "+label_name)
            im_data = np.reshape(im_data, [3, 32, 32])
            im_data = np.transpose(im_data, [1, 2, 0])

           # cv2.imshow("im_data", cv2.resize(im_data, (200, 200)))
           # cv2.waitKey(0)
            if not os.path.exists("{}/{}".format(test_path, label_name)):
                os.mkdir("{}/{}".format(test_path, label_name))
            cv2.imwrite("{}/{}/{}".format(test_path, label_name, file_name.decode('utf-8')), im_data)




if __name__ == '__main__':
    # 第一次运行需要根据加载测试集 和训练集
    # save_train_data()
    # save_test_data()
    # print("start")
    data_loader_test()