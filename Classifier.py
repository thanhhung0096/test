from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
class classifier():
    def __init__(self,hist,labels):
        hist = np.asarray(hist)
        labels = np.array(labels)
        labels = np.reshape(labels, (len(labels),1))
        self.data = np.concatenate((hist,labels), axis=1)
        np.random.shuffle(self.data)

        size = int(0.8*len(self.data))
        self.train_X = self.data[0:size,0:-1]
        self.train_Y = self.data[0:size, -1]
        self.test_X = self.data[size:-1,0:-1]
        self.test_Y = self.data[size:-1, -1]

    def svm(self):
        clf = LinearSVC(C=100.0, random_state=42)
        # clf = RandomForestClassifier(n_estimators=5)
        clf.fit(self.train_X,self.train_Y)
        predict = clf.predict(self.test_X)
        acc = accuracy_score(self.test_Y,predict)
        print "accuracy using SVM: %.2f" %acc
    def random_forest(self):
        clf = RandomForestClassifier(n_estimators=7)
        clf.fit(self.train_X, self.train_Y)
        predict = clf.predict(self.test_X)
        acc = accuracy_score(self.test_Y, predict)
        print "accuracy using Random Forest: %.2f" % acc

    def KNN(self):
        clf = KNeighborsClassifier()
        clf.fit(self.train_X, self.train_Y)
        predict = clf.predict(self.test_X)
        acc = accuracy_score(self.test_Y, predict)
        print "accuracy using kNN: %.2f" % acc

    def Bayes(self):
        clf = GaussianNB()
        clf.fit(self.train_X, self.train_Y)
        predict = clf.predict(self.test_X)
        acc = accuracy_score(self.test_Y, predict)
        print "accuracy using Naive Bayes: %.2f" % acc