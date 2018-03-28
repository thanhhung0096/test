from lbp import LBP
from Classifier import classifier
import cv2
import os
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
    image = cv2.imread("Capture.jpg",0)
    lbp = LBP(image)
    lbpImage,shape = lbp.createLBPImage()
    hist =  lbp.Histogram(lbpImage,True)
    faces,labels = ExtractFace(path)
    print labels
    hist_vectors = []
    for face in faces:
        start = time()

        lbp=LBP(face)
        lbpImage, shape = lbp.createLBPImage()
        print "created LBP image in %f second" %(time()-start)
        hist = lbp.Histogram(lbpImage, False)
        hist_vectors.append(hist)

    clf = classifier(hist_vectors,labels)
    clf.train()
    # test = cv2.imread("yaleB11_P00_Ambient.pgm",0)
    test = cv2.imread("yaleB11_P00A+035E+15.pgm", 0)
    # test = cv2.imread("images.jpg",0)
    lbp = LBP(test)
    lbpImage, shape = lbp.createLBPImage()
    hist = lbp.Histogram(lbpImage, False)
    hist = hist.reshape(1,-1)
    label = clf.predict(hist)
    print label
