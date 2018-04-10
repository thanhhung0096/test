import numpy as np
import time
import math
from scipy.spatial import distance

class Distance():
    Distances = (

    )
    def __init__(self,hist1, hist2):
        self.hist1 = hist1
        self.hist2 = hist2

    def Chi2(self):
        t = time.time()
        # compute the chi-squared distance
        # d =0
        # for (a,b) in zip(self.hist1 , self.hist2):
        #     if (a+b==0):
        #         continue
        #     d += 0.5 *( ((a-b)**2) / (a+b+1e-10) )
        # return the chi-squared distance
        # compute the chi-squared distance
        eps = 1e-10
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                          for (a, b) in zip(self.hist1, self.hist2)])
        print "Time compute chi2 distance: %f" %(time.time() - t)
        return d

    def Euclidean(self,weight = None):
        t = time.time()
        # d =  distance.euclidean(self.hist1 , self.hist2,weight)
        d = np.sqrt(np.sum([(a-b)**2  for (a,b) in zip(self.hist1,self.hist2)]))
        print "Time compute Euclidean distance: %f" % (time.time() - t)
        return d

    def Manhattan(self,weight=None):
        t = time.time()
        d = distance.cityblock(self.hist1,self.hist2,weight)
        # d = np.sum([np.abs( (a-b) for (a,b) in zip(self.hist1,self.hist2))])

        print "Time compute Manhatta distance: %f" % (time.time() - t)
        return d