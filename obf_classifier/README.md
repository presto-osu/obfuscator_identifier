## How to run
* copy the directory of apks into this folder. 
* type "bash preprocess.sh name/of/the/apks/folder"
* type "python classify.py | tee log"


## Prerequisites:
* Sklearing: http://scikit-learn.org/stable/install.html

There may be other required libraries. If you have any question, please
contact me.


To verify if the prerequest is met, I attached a test folder calld "test_apk".
So run it:
* bash preprocess.sh test_apk
* python classify.py | tee log

Then the result will be shown in both the screen and in the file called "log"
under this directory. 

## Note:
The preprocess part may be time consuming if the number of apks is large.
There are five kinds of label:
* Original ( not obfuscated by any of the four ones. We assume it has no obfuscation. But in fact, it may be obfuscated by other obfuscator) 
* Proguard
* Allatori
* Legu
* Bangcle

