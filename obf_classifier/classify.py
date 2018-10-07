from sklearn.externals import joblib
import numpy as np
import sys 

def main():
  fn = 'test.data'
  clf = joblib.load('classifier.pkl')
  param_clf = joblib.load('filter.pkl')
  X,Y = readVec(fn)
  predict(X, Y, clf, param_clf)

def predict(X, Y, clf, model): 
  X= np.array(X)
  total_for_each = {} 
  if model!=None:
    X = model.transform(X)
  res= []
  for v in X:
   r = clf.predict([v])
   res.append(r[0])
  match = 0
  for i in xrange(len(res)):
   total_for_each.setdefault(res[i],[]).append(Y[i])

  for i in total_for_each:
    print "Obfuscator: " + i + "  " + str(len(total_for_each[i]))
    print "------------------------------------"
    for j in total_for_each[i]:
      print j[:-4]
    print '\n'

def readVec(fn):
 X=[]
 Y=[]
 f = open(fn)
 content = f.readlines()
 for line in content:
  line = line.rstrip()
  splits = line.split(',')
  v = []
  size = len(splits)
  for i in xrange(size-3):
   v.append(int(splits[i]))
#  v.append(float(splits[size-2]))
  Y.append(splits[size-1]) 
  X.append(v)
 return X,Y
 
if __name__ == "__main__":
  main()
