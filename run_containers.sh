#!/usr/bin/env bash

# sudo docker run -d -p 9000:9000 -p 4040-4044:4040-4044 --name=user0 andypetrella/spark-notebook:0.9.0-SNAPSHOT-scala-2.11.8-spark-2.2.0-hadoop-2.7.2
N=$1

for (( i=1; i<=$N; i++ ))
do
    nt_port=$((9000 + i))
    sparkui_port=$((4040 + i))
    sudo docker run -d -p ${nt_port}:9000 -p ${sparkui_port}:4040 --name=user${i} training
done



# sudo docker stop $(sudo docker ps -a -q)
# sudo docker rm $(sudo docker ps -a -q)
