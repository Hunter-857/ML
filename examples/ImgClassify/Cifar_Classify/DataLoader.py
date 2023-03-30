# -*- coding: utf-8 -*-
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import glob

label_name= [
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
label_dict = {
    "airplane": 0,
    "automobile": 1, "bird": 2,
    "cat": 3, "deer": 4, "dog": 5, "frog": 6,
    "horse": 7, "ship": 8, "truck": 9}


train_transform =transforms.Compose([
    transforms.RandomCrop((28, 28)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.RandomRotation(90),
    transforms.RandomGrayscale(),
    transforms.ColorJitter(0.3, 0.3, 0.3, 0.3),
    transforms.ToTensor()
])
def deafult_loader(path):
    return Image.open(path).convert("RGB")
class CIFARDataSet(Dataset):
    def __init__(self,
                 im_list,
                 transform=None,
                 loader = deafult_loader):
        super(CIFARDataSet,self).__init__()
        self.transforme = None

        imgs = []
        for item in im_list:
            im_label_name = item.split("\\")[-2] # 图片的文件名
            imgs.append([item, label_dict[im_label_name] ])
            # print(item)
        self.imgs = imgs
        self.transform = transform
        self.loader = loader

    def __getitem__(self, index):
        im_path, im_label = self.imgs[index]
        im_data = self.loader(im_path)
        if self.transforme is not None:
            im_data = self.transforme()

        return im_data, im_label
    def __len__(self):
        return len(self.imgs)
def data_loader_test():
    im_train = glob.glob("data/train_data/*/*.png")
    im_test = glob.glob("data/test_data/*/*.png")
    train_data_set = CIFARDataSet(im_train, transform=train_transform)
    test_data_set = CIFARDataSet(im_test, transform=transforms.ToTensor)

    train_data_loader = DataLoader(dataset=train_data_set,
                                   batch_size=6,
                                   shuffle=True,
                                   num_workers=4)
    test_data_loader = DataLoader(dataset=test_data_set,
                                   batch_size=6,
                                   shuffle=False,
                                   num_workers=4)

    print("num of train", train_data_loader.__len__())
    print("num of train", test_data_loader.__len__())