This is a machine-learning approach to detect Android obfuscator. 

It is described in the paper “Who Changed You? Obfuscator Identification for Android” by Yan Wang and Atanas Rountev, which appeared at the IEEE/ACM International Conference on Mobile Software Engineering and Systems (MOBILESoft'17) \[[PDF](http://web.cse.ohio-state.edu/presto/pubs/msoft17.pdf)\] \[[BibTeX](http://web.cse.ohio-state.edu/presto/pubs/msoft17.bib)\].

## Structure
* obf_classifier is the folder of the tool. A README.txt file is in the folder for more instructions on how to use this tool
* dex_parser_src.zip contains the Java source code of the dex parser used in the tool
* learning.py is the Python script to generate the training model based on the training data. The generated model has two files: filter.pkl and classifier.pkl. Two default ones are in the "obf_classifier". 
* The APK files could be found in https://github.com/presto-osu/orlis-orcis/tree/master/orlis/open_source_benchmarks

## Prerequisites
 * [Python 2.7](https://www.python.org/download/releases/2.7/)
 * JDK1.8 or later
