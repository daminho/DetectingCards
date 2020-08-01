#Import


import torch
import numpy as np
import random as random
import torchvision.transforms as transforms
from torchvision.utils import save_image
from customDataset import Cards

#Load Data

my_transforms = transforms.Compose([
	transforms.ToPILImage(),
	transforms.Resize((256,256)),
	transforms.RandomCrop((224,224)),
	transforms.ColorJitter(brightness = np.random.uniform(0.4,0.6),contrast = np.random.uniform(0.4,0.6),saturation = np.random.uniform(0.4,0.6),hue = np.random.uniform(0.4,0.6)),
	transforms.RandomRotation(degree = np.random.uniform(0,359)),
	transforms.RandomHorizontalFlip(p=0.5),
	transforms.RandomVerticalFlip(p=0.05),
	transforms.RandomGreyScale(p=0.2),
	transforms.ToTensor(),
	transforms.Normalize(mean=[0.0, 0.0, 0.0], std=[1.0,1.0,1.0])
	])

dataset = Cards(csv_file = 'Cards.csv', root_dir = 'Cards', transforms = my_transforms)

img_num = 0
for _ in range(50):
	for im, label in dataset:
		save_image(img, 'img'+str(ing_num)+'.png')
		img_num += 1	