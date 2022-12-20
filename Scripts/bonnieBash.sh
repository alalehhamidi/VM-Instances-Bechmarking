# ./bin/sh
for i in {1..5}
do
    echo "the $i test is running...."
    bonnie++ -r 2G -s 4G -u ubuntu > bonnie_$i.txt
    sleep 5
done
