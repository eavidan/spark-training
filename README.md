# Spark Training with Notebooks

## Docker proxy
```
> cat <<EOF | sudo tee -a /etc/sysconfig/docker
http_proxy=http://proxy-chain.intel.com:911
https_proxy=https://proxy-chain.intel.com:911
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
> sh run_containers.sh [number of users]
```