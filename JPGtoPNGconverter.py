"""creating a jpg to png converter"""
import sys
import os

from PIL import Image


# dirs = sys.argv
IMAGE_DIR = sys.argv[1]
DEST_DIR = sys.argv[2]

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

for imagePath in os.listdir(IMAGE_DIR):
    imageName = os.path.splitext(imagePath)[0]
    img = os.path.join(IMAGE_DIR, imagePath)
    orig_img = Image.open(img)
    orig_img.save(f'{DEST_DIR}/{imageName}.png','png')
    print('all Done!')
