#!/bin/bash

echo "y" | apt-get update
echo "y" | apt-get install python3.7
echo "y" | apt-get install python-pip
echo "y" | apt-get install speedtest-cli


for i in {1..5}
do

sudo speedtest-cli --simple >> /home/ubuntu/speedtestOutput3
sleep 5
done