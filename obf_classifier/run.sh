base=`pwd`
dir=$(basename $1).res
mkdir $dir
for f in $1/*
do
 echo ${base}/$f
 fn=$(basename $f)
 java -jar wy.jar ${base}/$f ${base}/${dir}/${fn}.txt $2
done




