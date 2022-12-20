#!/bin/bash

echo "y" | sudo apt-get update
echo "y" |sudo apt install hdparm


for i in {1..5}
do
echo 1 > /proc/sys/vm/drop_caches
echo 2 > /proc/sys/vm/drop_caches
echo 3 > /proc/sys/vm/drop_caches
sudo hdparm -Tt /dev/xvda >> /home/ubuntu/hdparmOutput3
sleep 5
#sudo hdparm -Tt /dev/xvda1 >> /home/ubuntu/hdparmOutput
#sleep 5
done

