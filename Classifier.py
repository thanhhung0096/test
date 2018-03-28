from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
class classifier():
    def __init__(self,data,label):
        self.data = data
        self.label = label
    def train(self):
        clf = LinearSVC(C=100.0, random_state=42)
        # clf = RandomForestClassifier(n_estimators=5)
        clf.fit(self.data,self.label)
        print clf
        self.clf = clf

    def predict(self,featureVector):
        label = self.clf.predict(featureVector)
        return label



