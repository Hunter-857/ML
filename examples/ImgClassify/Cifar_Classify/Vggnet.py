# -*- coding: utf-8 -*-
'''
VGGNet是由牛津大学视觉几何组（Visual Geometry Group）于2014年提出的一个卷积神经网络模型。它在当时的ImageNet比赛中取得了第二名的好成绩。
VGGNet的主要贡献是证明了更深层的网络可以更好地提取图像特征，通过增加网络的深度和参数量，显著提升了图像分类任务的性能。
VGGNet包含了多个卷积层和全连接层，其中卷积层全部采用3×3的卷积核，并使用较小的步长和填充大小，
这样可以减少网络参数量和计算量，同时提高特征提取能力。在卷积层之后，使用ReLU激活函数进行非线性映射，并使用池化层对特征图进行下采样。
最后通过全连接层进行分类或回归任务。在训练过程中，采用Dropout和数据增强等技术进行模型正则化和防止过拟合。
VGGNet有多个版本，其中VGG16和VGG19是最为流行的版本，它们分别包含16个和19个卷积层，具有更深的网络结构和更高的准确率。

Very Deep Convolutional Networks for Large-Scale Image Recognition (VGGNet)：https://arxiv.org/abs/1409.1556

Going Deeper with Convolutions：https://arxiv.org/abs/1409.4842

VGG Network：https://neurohive.io/en/popular-networks/vgg16/

Understanding VGG Network：https://medium.com/analytics-vidhya/understanding-vgg-network-48bbc18a9ac5

A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way (Part 2)：
https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 (Part 2 中有介绍 VGG 网络)

'''

import torch
import  torch.nn as  nn
import  torch.nn.functional as  F

class VGGbase(nn.Module):
    def __init__(self):
        super(VGGbase,self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.max_pooling1 =nn.MaxPool2d(kernel_size=2, stride=2)
        # 14 * 14
        self.conv2_1 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.conv2_2 = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.max_pooling2 =nn.MaxPool2d(kernel_size=2, stride=2)

        # 7 * 7
        self.conv3_1 = nn.Sequential(
            nn.Conv2d(64, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.conv3_2 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.max_pooling3 = nn.MaxPool2d(kernel_size=2, stride=2)

        # 7 * 7
        self.conv4_1 = nn.Sequential(
            nn.Conv2d(256, 521, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(521),
            nn.ReLU()
        )
        self.conv4_2 = nn.Sequential(
            nn.Conv2d(256, 521, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(521),
            nn.ReLU()
        )
        # batchsize  -->
        self.fc = nn.Linear(512 *4 ,10)
    def forward(self, x):
        batchsize = x.size(0)
        out = self.conv1(x)
        out = self.max_pooling1(out)

        out = self.conv2_1(out)
        out = self.conv2_2(out)
        out = self.max_pooling2(out)

        out = self.conv3_1(out)
        out = self.conv3_2(out)
        out = self.max_pooling3(out)

        out = self.conv4_1(out)
        out = self.conv4_2(out)
        out = self.max_pooling4(out)

        out = out.view(batchsize,-1)
        out = self.fc(out)
        out = F.softmax(out, dim=1)
        return out