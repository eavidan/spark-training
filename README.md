# Spark Training with Notebooks

## Docker proxy
```
> cat <<EOF | sudo tee -a /etc/sysconfig/docker
http_proxy=yourproxy:port
https_proxy=yourproxy:port
no_proxy=10.*
EOF

> sudo service docker restart
```

## Setting up the notebooks
```
> git clone https://github.com/eavidan/spark-training.git
> cd spark-training
> wget https://ckannet-storage.commondatastorage.googleapis.com/2015-04-26T22:07:22.853Z/pageviews-by-second-tsv.gz
> gunzip pageviews-by-second-tsv.gz
> docker build -t training .
```
```
> nohup python site.py &
```

kill all containers
```
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
```
