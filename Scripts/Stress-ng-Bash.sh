# ./bin/sh
for i in {1..5}
do
	echo "the $i test is running..."
	stress-ng --cpu 4 --io 2 --vm 7000 --vm-bytes 15G --timeout 60s --metrics-brief>strng_$i.txt
	sleep 5	
done

