from matplotlib import pyplot as plt
from matplotlib import image as image
from matplotlib import collections as mc
from PIL import Image,ImageOps,ImageEnhance
import mahotas as mh
import cv2
import numpy as np
import argparse

def run(img_file, write_img, type):
	preprocessed_img = image_preprocessing(img_file,type)
def image_preprocessing(img_file, type):
	img = Image.open(img_file)
	plt.imshow(img)
	plt.show()
	print(img.shape)
	return img
def blob_detection(preprocessed_img):
	pass
def write_to_file(write_img):
	pass
def main():
    global args
    parser = argparse.ArgumentParser(description='...')
    parser.add_argument("-f", "--file",
                    help="image file to read",
                    type=str, default=None)
    parser.add_argument("-w", "--write_file",
                    help="image file to write to",
                    type=str, default=None)
    parser.add_argument("-t", "--type",
                    help="type of image file",
                    type=str, default="RGBA")
    args = parser.parse_args()
    run(args.file,args.write_file,args.type)

if __name__ == "__main__":
    main()