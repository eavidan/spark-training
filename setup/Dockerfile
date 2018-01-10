FROM andypetrella/spark-notebook:0.9.0-SNAPSHOT-scala-2.11.8-spark-2.2.0-hadoop-2.7.2

COPY ../overview /opt/docker/notebooks

wget https://ckannet-storage.commondatastorage.googleapis.com/2015-04-26T22:07:22.853Z/pageviews-by-second-tsv.gz
gunzip pageviews-by-second-tsv.gz

COPY ./pageviews-by-second-tsv /opt/docker/notebooks
