import cv2
import numpy as np
import time
from skimage import feature
class LBP():
    def __init__(self, image):
        self.image = image


    def createLBPImage(self):
        (rows, cols) = self.image.shape
        lbp_image = np.zeros((rows,cols),np.uint8)

        for row in range(1, rows - 2):
            for col in range(1, cols - 2):

                center_point = self.image[row][col]
                pixel7 = self.image[row - 1][col] > center_point
                pixel6 = self.image[row - 1][col - 1] > center_point
                pixel5 = self.image[row][col - 1] > center_point
                pixel4 = self.image[row + 1][col - 1] > center_point
                pixel3 = self.image[row + 1][col] > center_point
                pixel2 = self.image[row + 1][col + 1] > center_point
                pixel1 = self.image[row][col + 1] > center_point
                pixel0 = self.image[row - 1][col + 1] > center_point

                center_point = pixel7 * 128 + pixel6 * 64 + pixel5 * 32 + pixel4 * 16 + \
                               pixel3 * 8 + pixel2 * 4 + pixel1 * 2 + pixel0 * 1
                # lbp_image[row][col] = center_point
                lbp_image.itemset((row, col), center_point)
        # lbp_image = feature.local_binary_pattern(self.image,8, 1,method='uniform')

        return lbp_image,lbp_image.shape

    def Histogram(self,lbp_image,normalize=True):
        """

        :rtype: object
        """
        hist,_ = np.histogram(lbp_image,256,[0,256])
        if(normalize):
            hist = hist.astype("float")
            hist /= (hist.sum()+1e-7)
        return hist
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def __enter__(self):
        pass