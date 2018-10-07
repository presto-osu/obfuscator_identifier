from sklearn import svm
from sklearn.externals import joblib
import time
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.multiclass import OneVsRestClassifier
from matplotlib.font_manager import FontProperties
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import LinearSVC
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
import numpy as np
from tabulate import tabulate
import random
import sys

def readVec(fn):
 X=[]
 Y=[]
 f = open(fn)
 content = f.readlines()
 random.shuffle(content)
 for line in content:
  line = line.rstrip()
  splits = line.split(',')
  v = []
  size = len(splits)
  for i in xrange(size-3):
   v.append(int(splits[i]))
  Y.append(splits[size-1]) 
  X.append(v)
 return X,Y


def training(clf_param,clf,X,Y):
 Y = np.array(Y)
 X = np.array(X)
 clf_param = clf_param.fit(X, Y)
 model = SelectFromModel(clf_param, prefit=True)
 X = model.transform(X)
 #print type(clf_param).__name__ + str(X.shape)
 clf = clf.fit(X, Y)
 #print "classType: " +type(clf).__name__
 return clf,model

def predict(X, Y, clf, model): 
  X= np.array(X)
  total_for_each = {} 
  if model!=None:
    X = model.transform(X)
  res= []
  for v in X:
   r = clf.predict([v])
   res.append(r[0])
  return res

def genData(X,Y,start, end):
 X2 = X[start:end]
 Y2 = Y[start:end]
 if start-1>0:
  X1 = X[:start-1]
  Y1 = Y[:start-1]
 else:
  X1 = []
  Y1 = []
 if end<len(X):
  X1.extend(X[end:])
  Y1.extend(Y[end:])
 return X1,Y1,X2,Y2

   
def crossValidation(fn, n,type_of_clf, type_of_param_clf):
 ret = []
 X,Y = readVec(fn)
 scores = cross_val_score(type_of_clf, X, Y, cv=n) 
 print "Accuracy: " +str(scores.mean()) +" " + str(scores.std())
# scores = cross_val_score(type_of_clf, X, Y, cv=10, scoring ='f1_micro') 
# print "F1 micro: " +str(scores.mean()) +" " + str(scores.std())
# scores = cross_val_score(type_of_clf, X, Y, cv=10, scoring ='f1_macro') 
# print "F1 macro: " +str(scores.mean()) +" " + str(scores.std())
# return scores.mean(), scores.std(), time.time()-start

 clf, model = training(type_of_param_clf,type_of_clf,X,Y)
 joblib.dump(clf,'classifier.pkl')
 joblib.dump(model,'filter.pkl')
 return 

def doIt(): 
# feature selection method
 clf_para=[]
 clf_para.append(LinearSVC())
# clf_para.append(ExtraTreesClassifier())
# clf_para.append(DecisionTreeClassifier())
# clf_para.append(RandomForestClassifier())
# clf_para.append(LinearSVC(C=0.01,penalty="l2", dual=False))
# clf_para.append(linear_model.LogisticRegression(C=0.01,penalty="l2"))
	
# classifiers
 clfs = [
    SVC(),
#    KNeighborsClassifier(5,n_jobs=-1),
#    LinearSVC(C=1),
#    GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True, n_jobs=-1, copy_X_train=False), #slow
#    ExtraTreesClassifier(),
#    DecisionTreeClassifier(),
#    OneVsRestClassifier(LinearSVC()),
#    RandomForestClassifier(),
#    MLPClassifier(),
#    AdaBoostClassifier(),
#    GaussianNB(),
#    QuadraticDiscriminantAnalysis(),
#    OneVsRestClassifier(linear_model.LogisticRegression()),
#    LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')
  ]

 data = []
 tools = []
 data_fn = sys.argv[1]
 num = 10 

 for clf2 in clf_para:
  for clf1 in clfs:
    crossValidation(data_fn,num,clf1, clf2)

if __name__ == "__main__":
  doIt()
