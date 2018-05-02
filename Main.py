from lbp import LBP
from Classifier import classifier
import numpy as np
import cv2
import os
from Classifier import classifier
from time import time
import numpy as np
path = 'KL/Faces'
def ExtractFace(pathToData):
    ""
    faces=[]
    labels=[]
    folders = os.listdir(pathToData)
    for folder in folders:
        label = int(folder.replace("s", ""))
        images = os.listdir(pathToData +"/" + folder)
        for img in images:
            path = pathToData +"/"+ folder + "/" + img
            # print path
            image = cv2.imread(path,0)
            ##            print type(image)
            # cv2.imshow("Training on image...", image)
            # cv2.waitKey(100)
            # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ##                print type(face)
            labels.append(label)
            faces.append(image)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.destroyAllWindows()
    return faces, labels
if __name__ == '__main__':
    faces, labels = ExtractFace('KL/Faces')
    lbp_images = []
    for face in faces:
        lbp = LBP(face)
        lbp_image,_ = lbp.createLBPImage()
        lbp_images.append(lbp.Histogram(lbp_image))

    clf = classifier(lbp_images, labels)
    clf.svm()
    clf.random_forest()
    clf.KNN()