from distance import Distance
from lbp import LBP
import cv2
import time
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import local_binary_pattern
from scipy.stats import chisquare
from lbp import LBP
image = cv2.imread("yaleB12_P00A+035E+40.pgm",0)
lbp1= local_binary_pattern(image,8,1,method='uniform')
lbp2 = LBP(image)
eps = 1e-9
cv2.imshow("lbp1" ,lbp1)
cv2.imshow("lbp2" ,lbp2.createLBPImage()[0])
hist1,_ = np.histogram(lbp1, bins=np.arange(0,11) , range=[0,10])
hist2,_ = np.histogram(lbp2, bins=np.arange(0,11) , range=[0,10])
hist1 = hist1.astype("float")
hist2 = hist2.astype("float")
hist1 /= (hist1.sum() + eps)
hist2 /= (hist2.sum() + eps)
print len(lbp1.ravel())
print type(lbp1)
# print chisquare(hist1,hist2)

cv2.waitKey(0)