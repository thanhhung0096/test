from distance import Distance
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import local_binary_pattern
from scipy.stats import chisquare
from lbp import LBP
image = cv2.imread("KL\Faces\s1\yaleB11_P00_Ambient.pgm",0)
print type(image)
# cv2.imshow('a',image)
# cv2.waitKey(0)
# image = np.array((image))
# print type(image)
#
lbp_image = local_binary_pattern(image,8,1)
cv2.imshow("1",lbp_image)

# image2 = cv2.imread("26.png",0)
#
# lbp_image2 = local_binary_pattern(image2,8,1)
# # cv2.imshow("2",lbp_image)
#
# hist1,_ = np.histogram(lbp_image, bins=256,range=[0,256])
# hist2,_ = np.histogram(image2, bins=256, range=[0,256])
#
# dis = Distance(hist1,hist2)
#
# print "Chi Square: ",dis.Chi2()
# print "Euclidean: ",dis.Euclidean(None)
# print "Manhatta: " ,dis.Manhattan()

# print zip(hist1)
cv2.waitKey(0)