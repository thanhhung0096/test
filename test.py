import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("images.jpg",0)
lbp_image = cv2.imread("images.jpg",0)
(rows, cols) = image.shape
count=1
for row in range(1,rows-2):
    for col in range(1,cols-2):
        center_point = image[row][col]
        pixel7 = image[row - 1][col] > center_point
        pixel6 = image[row - 1][ col-1] > center_point
        pixel5 = image[row][ col - 1] > center_point
        pixel4 = image[row+1][col-1] > center_point
        pixel3 = image[row + 1][ col] > center_point
        pixel2 = image[row + 1][col+1] > center_point
        pixel1 = image[row ][col + 1] > center_point
        pixel0 = image[row-1][col +1] > center_point


        center_point = pixel7*128+pixel6*64+pixel5*32+pixel4*16+ \
                       pixel3 * 8 + pixel2*4+ pixel1*2+ pixel0*1
        # lbp_image[row][col] = center_point
        lbp_image.itemset((row,col),center_point)
hist,bins = np.histogram(lbp_image.flatten(),256,[0,256])
hist = hist.astype("float")
hist /= (hist.sum()+1e-7)
print hist

