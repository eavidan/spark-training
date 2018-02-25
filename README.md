# Spark Training with Notebooks
This repo explains how to setup spark notebook enviroments on a single server.
Each environment will be created in a different container with its own resources (currently 3 CPUs).

## Docker proxy
in case your server is behind a proxy, run the following
```
> cat <<EOF | sudo tee -a /etc/sysconfig/docker
http_proxy=yourproxy:port
https_proxy=yourproxy:port
no_proxy=10.*
EOF

> sudo service docker restart
```

## Setting up the notebooks environment
Log in the server we is allocated to the training.
This server should have as many CPU cores as possible, as each participant will consume a few.
Run the following line, which will create the docker image that will be used with all the notebooks.
currently only the overview folder will be copie to the notebooks main folder
```
> git clone https://github.com/eavidan/spark-training.git
> cd spark-training
# download a data file to be copied into the docker image
> wget https://ckannet-storage.commondatastorage.googleapis.com/2015-04-26T22:07:22.853Z/pageviews-by-second-tsv.gz
> gunzip pageviews-by-second-tsv.gz
> docker build -t training .
```
Now, run the website that execute the containers
```
> nohup python site.py &
```
brawse to `http://[server address]:8080`
## Some more commands
### kill all containers
```
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
```
### See all running enviroments and their links
```
http://[server address]:8080/list
```