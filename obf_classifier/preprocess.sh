bash parse_apk.sh $1 
target=${1%/}
rm test.data
bash create_test_data.sh ${target}.res 
