#!/usr/bin/env bash
# cat <<EOF | sudo tee -a /etc/sysconfig/docker
# http_proxy=http://proxy-chain.intel.com:911
# https_proxy=https://proxy-chain.intel.com:911
# no_proxy=10.*
# EOF

# sudo service docker restart

# sudo docker pull andypetrella/spark-notebook:0.9.0-SNAPSHOT-scala-2.11.8-spark-2.2.0-hadoop-2.7.2

# sudo docker run -d -p 9000:9000 -p 4040-4044:4040-4044 --name=user0 andypetrella/spark-notebook:0.9.0-SNAPSHOT-scala-2.11.8-spark-2.2.0-hadoop-2.7.2
N = 20

for i in `seq 0 ${N}`;
do
    nt_port=$((9000 + i))
    sparkui_port_from=$((4040 + $((i * 5))))
    sparkui_port_to=$((sparkui_port_from + 5))
    sparkui_port_from=$((sparkui_port_from + 1))
    sudo docker run -d -p ${nt_port}:9000 -p ${sparkui_port_from}-${sparkui_port_to}:4040-4044 --name=user${i} training
done


sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
