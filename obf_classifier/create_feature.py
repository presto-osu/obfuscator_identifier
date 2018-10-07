import os
import sys

class FeatureVector:
 def __init__(self):
   self.string = []
   self.pkg = []
   self.cls = []
   self.field = []
   self.method = []
   self.files = []
   self.clsSig = []
   self.exField= []
   self.exMethod = []
   self.exPkg = []
   self.exCls = []
   self.exClsSig = []


 def doExClsSig(self, s):
   ret = [] 
   for i in self.exClsSig:
     if i in s:
      ret.append(1)
     else:
      ret.append(0)
   return ret

 def doExCls(self, s):
   ret = []
   for i in self.exCls:
    if i in s :
     ret.append(1)
    else:
     ret.append(0)
   return ret

 def doExPkg(self, s):
   ret= []
   for i in self.exPkg:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret

 def doClsSig(self, s):
   ret = []
   for i in self.clsSig:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret

 def doExField(self, s):
   ret = []
   for i in self.exField:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret
  
 def doExMethod(self, s):
   ret = []
   for i in self.exMethod:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret
 
 def doString(self,s):
   ret = []
   for i in self.string:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret 

 def doPkg(self,s):
   ret = []
   for i in self.pkg:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret
 
 def doCls(self, s):
   ret = []
   for i in self.cls:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret

 def doMethod(self, s):
   ret = []
   for i in self.method:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret

 def doField(self, s):
   ret = []
   for i in self.field:
    if i in s:
      ret.append(1)
    else: 
      ret.append(0)
   return ret

 def doFiles(self, s):
   ret = []
   for i in self.files:
    if i in s:
     ret.append(1)
    else:
     ret.append(0)
   return ret

  
class Feature:
 def __init__(self):
   self.string = set()
   self.pkg = set()
   self.cls = set()
   self.field = set()
   self.method = set()
   self.files = set()
   self.clsSig = set()
   self.exField = set()
   self.exMethod = set()
   self.exCls = set()
   self.exPkg = set()
   self.exClsSig = set()
 
 def getFeature(self):
   ret = FeatureVector()
   for i in self.clsSig:
    ret.clsSig.append(i)
   for i in self.files:
    ret.files.append(i)
   for i in self.pkg:
    ret.pkg.append(i)
   for i in self.cls:
    ret.cls.append(i)
   for i in self.method:
    ret.method.append(i)
   for i in self.field:
    ret.field.append(i)
   for i in self.string:
    ret.string.append(i)
   for i in self.exField:
    ret.exField.append(i)
   for i in self.exMethod:
    ret.exMethod.append(i)
   for i in self.exCls:
    ret.exCls.append(i)
   for i in self.exPkg:
    ret.exPkg.append(i)
   for i in self.exClsSig:
    ret.exClsSig.append(i)
   return ret

 def parseFile(self, fn):
  f = open(fn)
  cur_set = None
  for i, line in enumerate(f):
   line = line.rstrip().strip()
   if line == '-------------------fileName------------------':
    cur_set = self.files
    continue
   if line == '-------------------string------------------':
    cur_set = self.string
    continue
   if line == '-------------------pkgName------------------':
    cur_set = self.pkg
    continue
   if line == '-------------------clsName------------------':
    cur_set = self.cls
    continue
   if line == '-------------------methodName------------------':
    cur_set = self.method
    continue
   if line == '-------------------fieldName------------------': 
     cur_set = self.field 
     continue
   if line == '-------------------clsSig------------------':
    cur_set = self.clsSig
    continue
   if line == '-------------------exFieldName------------------':
    cur_set = self.exField
    continue
   if line == '-------------------exMethodName------------------':
    cur_set = self.exMethod
    continue
   if line == '-------------------exClsName------------------':
    cur_set = self.exCls
    continue
   if line == '-------------------exPkgName------------------':
    cur_set = self.exPkg
    continue
   if line == '-------------------exClsSig------------------':
    cur_set = self.exClsSig
    continue
   if line == '':
    continue
   cur_set.add(line)

class FeatureFromFile:
 def __init__(self):
   self.string = set()
   self.pkg = set()
   self.cls = set()
   self.field = set()
   self.method = set()
   self.files = set()
   self.clsSig = set()
   self.exField = set()
   self.exMethod = set()
   self.exPkg = set()
   self.exCls = set()
   self.exClsSig = set()

 def parseFile(self, fn):
  print fn
  f = open(fn)
  cur_set = None
  for i, line in enumerate(f):
   line = line.rstrip().strip()
   if i < 4:
    continue
   if line == '----------------fileName----------------':
    cur_set = self.files
    continue
   if line == '----------------string----------------':
    cur_set = self.string
    continue
   if line == '----------------pkgName----------------':
    cur_set = self.pkg
    continue
   if line == '----------------clsName----------------':
    cur_set = self.cls
    continue
   if line == '----------------methodName----------------':
    cur_set = self.method
    continue
   if line == '----------------clsSig----------------':
    cur_set = self.clsSig
    continue
   if line == '----------------externalFieldName----------------':
    cur_set = self.exField
    continue
   if line == '----------------externalMethodName----------------':
    cur_set = self.exMethod
    continue
   if line == '----------------externalClsName----------------':
    cur_set = self.exCls
    continue
   if line == '----------------externalPkgName----------------':
    cur_set = self.exPkg
    continue
   if line == '----------------externalClsSig----------------':
    cur_set = self.exClsSig
    continue
   if line == '':
    continue
   cur_set.add(line)

 def createFeatureVector(self, feature_vector):
   clsSig = feature_vector.doClsSig(self.clsSig)
   files = feature_vector.doFiles(self.files)
   pkg = feature_vector.doPkg(self.pkg)
   cls = feature_vector.doCls(self.cls)
   method = feature_vector.doMethod(self.method)
   field = feature_vector.doField( self.field)
   string = feature_vector.doString( self.string)
   exField = feature_vector.doExField(self.exField)
   exMethod = feature_vector.doExMethod(self.exMethod)
   exCls = feature_vector.doExCls(self.exCls)
   exPkg = feature_vector.doExPkg(self.exPkg)
   exClsSig = feature_vector.doExClsSig(self.exClsSig)
   return files+pkg+cls+method+field+string+exField+exMethod+exCls+exPkg+exClsSig

def writeToFile2(fn, vv, labels):
 f = open(fn,'a')
 for index,v in enumerate(vv):
  for i in v:
   f.write(str(i))
   f.write(',')
  f.write(labels[index])
  f.write('\n')
 f.close()

def writeToFile(fn, vv, label):
 f = open(fn,'a')
 for v in vv:
  for i in v:
   f.write(str(i))
   f.write(',')
  f.write(label)
  f.write('\n')
 f.close()

def getVectorForDir(base,feature_vector,files=[]):   
  vv = []
  for f in os.listdir(base):
   files.append(f)
   featureFromFile = FeatureFromFile()
   featureFromFile.parseFile(base+'/'+f)
   v = featureFromFile.createFeatureVector(feature_vector)
   vv.append(v)
  return vv

def createPlay(): 
 base = sys.argv[1]
 feature_files = ['proguard.feature','allatori.feature','legu.feature','bangcle.feature']
 feature = Feature()
 for f in feature_files:
   feature.parseFile(base+'/features/'+f)
 feature_vector = feature.getFeature()

 files = [] 
 vv = getVectorForDir(base+'/'+ sys.argv[2], feature_vector, files)
 writeToFile2('test.data', vv,files)


if __name__ == "__main__":
  createPlay()
